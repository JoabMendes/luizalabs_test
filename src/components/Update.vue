<template>
    <div id="new">
        <b-container>
            <b-row>
                <b-col cols="12" sm="10" md="10" lg="10" xl="10">
                    <h1 id="page-title">Update employee</h1>
                </b-col>
                <b-col cols="12" sm="2" md="2" lg="2" xl="2">
                    <b-button variant="outline-primary" id="cancel-btn" @click="goIndex()">
                        Cancel
                    </b-button>
                </b-col>
            </b-row>
            <b-row v-if="!employeeLoading">
                <b-col cols="12">
                    <b-list-group>
                        <b-list-group-item>
                            <form>
                                <b-form-group
                                        id="nameSet"
                                        label="Employee name:"
                                        label-for="name"
                                        :invalid-feedback="invalidNameFeedback"
                                        :state="nameState">
                                    <b-form-input id="name" :state="nameState" v-model.trim="employee_form.name">
                                    </b-form-input>
                                </b-form-group>
                                <b-form-group
                                        id="emilSet"
                                        label="Employee email:"
                                        label-for="email"
                                        :invalid-feedback="invalidEmailFeedback"
                                        :state="emailState">
                                    <b-form-input id="email" :state="emailState" v-model.trim="employee_form.email">
                                    </b-form-input>
                                </b-form-group>
                                <b-form-group id="DepartmentSet"
                                              label="Department:"
                                              label-for="departments">
                                    <multiselect v-model="selectedDepartment" :options="departments"
                                                 :show-labels="true"
                                                 :loading="loading"
                                                 placeholder="Select a department from the list"
                                                 label="name" track-by="id" :searchable="true"
                                                 >
                                    </multiselect>
                                </b-form-group>
                                <b-form-group id="ControlSet">
                                    <b-button type="button" variant="primary" @click="updateEmployee()"
                                              :disabled="submitEmployeeState || savingEmployee">
                                        {{savingEmployee ? 'Updating...' : 'Update'}}
                                    </b-button>
                                    <b-button type="button" variant="outline-danger" @click="deleteEmployee()">
                                        Delete
                                    </b-button>
                                </b-form-group>
                            </form>
                        </b-list-group-item>
                    </b-list-group>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>

    import axios from 'axios';

    export default {
        name: 'New',
        props: ['id'],
        data() {
            return {
                loading: true,
                employeeLoading: true,
                employee: null,
                employee_form: {
                    name: '',
                    email: '',
                    department: null,
                },
                departments: [],
                selectedDepartment: null,
                savingEmployee: false,
                // endpoints
                employeeEndpoint: '/api/v1/employee',
                departmentEndpoint: '/api/v1/department',
            }
        },
        beforeMount() {
            this.fetchDepartments();
        },
        methods: {
            goIndex() {
                this.$router.push({name: 'index'});
            },
            validateEmail(email) {
                let re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                return re.test(email);
            },
            fetchEmployee() {
                this.employeeLoading = true;
                let endpoint = this.employeeEndpoint + '/' + this.id;
                axios.get(endpoint).then(response => {
                    this.employee = response.data;
                    this.employee_form.name = this.employee.name;
                    this.employee_form.email = this.employee.email;
                    this.selectedDepartment = this.departments.find(d => d.id === this.employee.department.id);
                    this.employeeLoading = false;
                }).catch(error => {
                    console.log(error);
                    this.goIndex();
                })
            },
            fetchDepartments() {
                this.loading = true;
                let promises = [];
                promises.push(axios.get(this.departmentEndpoint).then(response => {
                    // handle success
                    return response.data;
                }));
                Promise.all(promises).then(responses => {
                    this.departments = responses[0];
                    this.loading = false;
                    this.fetchEmployee();
                });
            },
            resetForm() {
                this.employee_form = {
                    name: '',
                    email: '',
                    department: null,
                };
                this.selectedDepartment = null;
            },
            showErrorModal(message) {
                this.$swal('Ops!', message, 'error');
            },
            showSuccessModal(message) {
                this.$swal('Success!', message, 'success');
            },
            updateEmployee() {
                if (!this.submitEmployeeState && this.departmentState) {
                    this.employee_form.department = this.selectedDepartment.id;
                    let endpoint = this.employeeEndpoint + '/' + this.employee.id;
                    axios.put(endpoint, this.employee_form).then(response => {
                        if (response.data) {
                            let message = this.employee_form.name + " was added successfully updated!";
                            this.showSuccessModal(message);
                            this.goIndex();
                        }
                    }).catch(error => {
                        console.log(error);
                        this.showErrorModal(JSON.stringify(error));
                    });
                } else {
                    console.log(this.submitEmployeeState);
                    console.log(this.departmentState);
                    let message = "Form is invalid!\n";
                    if (!this.departmentState) {
                        message += "- Please select a department for this employee";
                    }
                    this.showErrorModal(message);
                }
            },
            deleteEmployee() {
                let employee = this.employee;
                this.$swal({
                    title: "Are you sure?",
                    text: "Once delete " + employee.name + ", you will not be able to recover this employee from the database!",
                    icon: "warning",
                    buttons: true,
                    dangerMode: true,
                }).then((willDelete) => {
                    if (willDelete) {
                        let endpoint = this.employeeEndpoint + '/' + employee.id;
                        axios.delete(endpoint).then(response => {
                            this.goIndex();
                        }).catch(error => {
                           console.log(error);
                           this.$swal(
                               "Oops! There was a problem whe trying to delete this employee. " +
                               "Please try again later"
                           );
                        });
                    }
                });
            }
        },
        computed: {
            nameState() {
                if (this.employee_form.name.length === 0) {
                    return null;
                }
                return this.employee_form.name.length > 2;
            },
            invalidNameFeedback() {
                return 'Please enter a name with at least 2 characters';
            },
            emailState() {
                if (this.employee_form.email.length === 0) {
                    return null;
                }
                return this.employee_form.email.length > 0 && this.validateEmail(this.employee_form.email);
            },
            invalidEmailFeedback() {
                if (this.employee_form.email.length > 0 && !this.validateEmail(this.employee_form.email)) {
                    return 'Please enter a valid email account'
                }
                return '';
            },
            departmentState() {
                return this.selectedDepartment !== null;
            },
            submitEmployeeState() {
                let fields = [
                    this.employee_form.name.length,
                    this.employee_form.email.length
                ];
                return !(fields.indexOf(0) === -1 && this.nameState && this.emailState);
            }
        }
    }
</script>

<style lang="scss">

    // Main colors
    $white: #fff;
    $luizaLabsBlue: #396EAF;
    $black: #201A16;
    $mainGrey: #808080;

    #page-title {
        font-size: 20px;
        margin-bottom: 30px;
    }

    #cancel-btn {
        float: right;
    }

    #ControlSet {
        button {
            float: right;
            margin-left: 15px;
        }
    }

</style>

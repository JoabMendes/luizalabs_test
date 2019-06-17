<template>
    <div id="new">
        <b-container>
            <b-row>
                <b-col cols="12" sm="10" md="10" lg="10" xl="10">
                    <h1 id="page-title">Add new employee</h1>
                </b-col>
                <b-col cols="12" sm="2" md="2" lg="2" xl="2">
                    <b-button variant="outline-primary" id="cancel-btn" @click="goIndex()">
                        Cancel
                    </b-button>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="12">
                    <b-list-group>
                        <b-list-group-item>
                            <form>
                                <b-form-group
                                        id="nameSet"
                                        label="Employee name:"
                                        label-for="name"
                                        :invalid-feedback="invalidNameFeedback"
                                        :valid-feedback="validNameFeedback"
                                        :state="nameState">
                                    <b-form-input id="name" :state="nameState" v-model.trim="employee_form.name">
                                    </b-form-input>
                                </b-form-group>
                                <b-form-group
                                        id="emilSet"
                                        label="Employee email:"
                                        label-for="email"
                                        :invalid-feedback="invalidEmailFeedback"
                                        :valid-feedback="validEmailFeedback"
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
                                    <b-button type="button" variant="primary" @click="submitNewEmployee()"
                                              :disabled="submitEmployeeState || savingEmployee">
                                        {{savingEmployee ? 'Saving...' : 'Save'}}
                                    </b-button>
                                    <b-button type="reset" variant="outline-primary" @click="resetForm()">
                                        Reset
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
        data() {
            return {
                loading: true,
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
            submitNewEmployee() {
                if (!this.submitEmployeeState && this.departmentState) {
                    this.employee_form.department = this.selectedDepartment.id;
                    axios.post(this.employeeEndpoint, this.employee_form).then(response => {
                        if (response.data) {
                            let message = this.employee_form.name + " was added successfully added to the database!";
                            this.showSuccessModal(message)
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
            validNameFeedback() {
                return this.nameState === true && this.employee_form.name.length > 0 ? 'Thank you!' : ''
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
            validEmailFeedback() {
                return this.emailState === true && this.employee_form.email.length > 0 ? 'Thank you!' : ''
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

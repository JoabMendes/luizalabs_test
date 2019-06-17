<template>
    <div id="index">
        <b-container>
            <b-row>
                <b-col cols="12" sm="10" md="10" lg="10" xl="10">
                    <h1 id="page-title">Registered employees</h1>
                </b-col>
                <b-col cols="12" sm="2" md="2" lg="2" xl="2">
                    <b-button variant="outline-primary" id="new-employee-btn" @click="goNew()">
                        New
                    </b-button>
                </b-col>
            </b-row>
            <b-row v-if="loading">
                <b-col cols="12">
                    <img src="/static/assets/loading.gif" alt="loading" id="loading">
                </b-col>
            </b-row>
            <b-row v-else>
                <b-col cols="12" v-if="employees.length > 0">
                    <b-list-group>
                        <b-list-group-item v-for="employee in employees" :key="employee.id">
                            <b-row>
                                <b-col cols="10" sm="10" md="10" lg="10" xl="10">
                                    <p class="employee-name">
                                        {{employee.name}}
                                        <span class="employee-email">{{employee.email}}</span>
                                    </p>
                                    <b-badge variant="primary">
                                        {{employee.department.name}}
                                    </b-badge>

                                </b-col>
                                <b-col cols="2" sm="2" md="2" lg="2" xl="2">
                                    <b-dropdown class="action-menu" size="sm" dropleft
                                                toggle-class="text-decoration-none" no-caret
                                                variant="primary">
                                        <template slot="button-content">
                                            <i class="fa fa-cog"></i><span class="sr-only">Action</span>
                                        </template>
                                        <b-dropdown-item-button @click="goUpdate(employee)">
                                            <i class="fa fa-edit"></i> Edit
                                        </b-dropdown-item-button>
                                        <b-dropdown-item-button @click="deleteEmployee(employee)">
                                            <i class="fa fa-trash"></i> Delete
                                        </b-dropdown-item-button>
                                    </b-dropdown>
                                </b-col>
                            </b-row>
                        </b-list-group-item>
                    </b-list-group>
                </b-col>
                <b-col cols="12" v-else>
                    <b-list-group>
                        <b-list-group-item>
                            <p id="empty">
                                There're no employees registered in the system yet<br/>
                                Select the 'New' option to add a new entry
                            </p>
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
        name: 'Index',
        data() {
            return {
                loading: true,
                employees: [],
                // endpoints
                employeeEndpoint: '/api/v1/employee'
            }
        },
        beforeMount() {
            this.fetchEmployees();
        },
        methods: {
            fetchEmployees() {
                this.loading = true;
                let promises = [];
                promises.push(axios.get(this.employeeEndpoint).then(response => {
                    // handle success
                    return response.data;
                }));
                Promise.all(promises).then(responses => {
                    this.employees = responses[0];
                    this.loading = false;
                });
            },
            deleteEmployee(employee) {
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
                            this.fetchEmployees();
                        }).catch(error => {
                           console.log(error);
                           this.$swal(
                               "Oops! There was a problem whe trying to delete this employee. " +
                               "Please try again later"
                           );
                        });
                    }
                });
            },
            goNew() {
                this.$router.push({name: 'new'});
            },
            goUpdate(employee) {
                this.$router.push({name: 'update', params: {id: employee.id}});
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

    #loading {
        width: 200px;
        margin: auto;
        display: block;
    }

    #page-title {
        font-size: 20px;
        margin-bottom: 30px;
    }

    .employee-name {
        margin-bottom: 0px;
    }

    .employee-email {
        font-size: 12px;
        color: $mainGrey;
        margin-bottom: 0px;
    }

    .action-menu {
        float: right;
    }

    #empty {
        padding-top: 10px;
        text-align: center;
    }

    #new-employee-btn {
        float: right;
    }

</style>

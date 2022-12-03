<template>

<div class="container-fluid row">
        
        <div class="col-md-8">

        </div>

        <div class="col-md-4">
            <br/>
            <h4>Login</h4>
            <hr/>
            <table>

                <tr>
                    <td>Username</td>
                    <td><input type="text" v-model="username" class="form-control"></td>
                </tr>

                <tr>
                    <td>Password</td>
                    <td><input type="password" v-model="password" class="form-control"></td>
                </tr>

                <tr>
                    <td></td>
                    <td>
                        <button class="btn btn-primary form-control" @click="login()">Login</button>
                    </td>
                </tr>
            </table>

        </div>

    </div>
  
  
  </template>
  
  <script>
  import axios from 'axios'
  import Swal from 'sweetalert2'

  export default {
    layout: 'master',
    name: 'Login',
    data() {
        return {
            username: '',
            password: ''
        }
    },

    methods: {

        // Login
        async login() {
            if (this.username != "" && this.password != "") {
                await axios({
                    method: 'POST',
                    url: this.$store.state.api + '/auth/auth_login',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    data: { 'username': this.username, 'password': this.password,},
                }).then((response) => {
                    var jsonData = JSON.parse(JSON.stringify(response.data));

                    if (jsonData['status'] == true) {
                        Swal.fire({
                            title: 'Success!',
                            text: 'You have been Authenticated Successfully',
                            icon: 'success',
                            confirmButtonText: 'Cool!'
                        }).then( () => {
                            // this.$store.store_auth_data({'auth_user': this.username, 'auth_token' : jsonData[]})
                            this.$store.commit('store_auth_data', {'auth_user': this.username, 'auth_token' : jsonData['auth_token']})

                            // this.$router.push('/user/dashboard');
                            window.location.assign('/user/dashboard');
                        });
                    }else {
                        Swal.fire({
                            title: 'Error!',
                            text: 'Please Enter Correct Username and Password Combination',
                            icon: 'error',
                            confirmButtonText: 'Ooh!'
                        })
                    }
                });
            }else {
                Swal.fire({
                    title: 'Error!',
                    text: 'Please Enter Username and Password Fields',
                    icon: 'error',
                    confirmButtonText: 'Ooh!'
                })
            }
          
        }
    }
   }
  </script>
  
<template>

    <div class="container-fluid row">
        
        <div class="col-md-8">

        </div>

        <div class="col-md-4">
            <br/>
            <h4>Create New Account</h4>
            <hr/>
            <table>
                <tr>
                    <td>First Name</td>
                    <td><input type="text" v-model="firstName" class="form-control"></td>
                </tr>

                <tr>
                    <td>Last Name</td>
                    <td><input type="text" v-model="lastName" class="form-control"></td>
                </tr>

                <tr>
                    <td>Email</td>
                    <td><input type="text" v-model="email" class="form-control"></td>
                </tr>

                <tr>
                    <td>Password</td>
                    <td><input type="password" v-model="password" class="form-control"></td>
                </tr>

                <tr>
                    <td>Verify Password</td>
                    <td><input type="password" v-model="verifyPassword" class="form-control"></td>
                </tr>

                <tr>
                    <td></td>
                    <td>
                        <button class="btn btn-primary form-control">Create New Account</button>
                    </td>
                </tr>
            </table>

        </div>

    </div>
    
  </template>
  
  <script>
  export default {
    layout: 'master',
    name: 'Register',
    data() {
        return {
            firstName: '',
            lastName: '',
            email: '',
            password: '',
            verifyPassword: ''
        }
    }
  }
  </script>
  
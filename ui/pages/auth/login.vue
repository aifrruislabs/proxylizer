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
                    <td>Email</td>
                    <td><input type="text" v-model="email" class="form-control"></td>
                </tr>

                <tr>
                    <td>Password</td>
                    <td><input type="password" v-model="password" class="form-control"></td>
                </tr>

                <tr>
                    <td></td>
                    <td>
                        <button class="btn btn-primary form-control">Login</button>
                    </td>
                </tr>
            </table>

        </div>

    </div>
  
  
  </template>
  
  <script>
  export default {
    layout: 'master',
    name: 'Login'
  }
  </script>
  
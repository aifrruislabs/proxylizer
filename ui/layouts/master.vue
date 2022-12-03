<template>
    <div>

    <nav class="navbar navbar-expand-lg navbar-custom">
      <div class="container-fluid">
        <nuxt-link class="navbar-brand" to="/">Proxylizer</nuxt-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li v-show="is_authenticated" class="nav-item">
              <nuxt-link class="nav-link active" aria-current="page" to="/user/dashboard">Dashboard</nuxt-link>
            </li>

            <li v-show="is_authenticated" class="nav-item">
              <nuxt-link class="nav-link active" aria-current="page" to="/user/container">Containers</nuxt-link>
            </li>
          
            <li v-show="!is_authenticated" class="nav-item">
              <nuxt-link class="nav-link active" aria-current="page" to="/">Home</nuxt-link>
            </li>
          </ul>

          <ul class="navbar-nav navbar-right mb-2 mb-lg-0">
            <li v-show="is_authenticated" class="nav-item">
              <nuxt-link class="nav-link active" aria-current="page" to="#">Welcome {{ auth_user }}</nuxt-link>
            </li>

            <li v-show="is_authenticated" class="nav-item">
              <a class="nav-link active" aria-current="page" @click="logout()">Logout</a>
            </li>


            <li v-show="!is_authenticated" class="nav-item">
              <nuxt-link class="nav-link active" aria-current="page" to="/auth/login">Login</nuxt-link>
            </li>

            <li v-show="!is_authenticated" class="nav-item">
              <nuxt-link class="nav-link active" aria-current="page" to="/auth/register">Create New Account</nuxt-link>
            </li>
            
          </ul>
          
        </div>
      </div>
    </nav>

      <Nuxt/>
    </div>
</template>


<script>

import axios from 'axios'
import Swal from 'sweetalert2'

export default {

  name: 'Master',
  data() {
    return {
      user: 'Proxy User',
      auth_user : this.$store.state.auth_user,
      is_authenticated: this.$store.state.is_authenticated
    }
  }, 

  methods: {

    // Logout
    async logout() {
      alert("Hello Buddy");

      await axios({
          method: 'POST',
          url: this.$store.state.api + '/auth/auth_logout',
          headers: {
              "Content-Type": "application/json",
          },
          data: { 'username': this.username, 'token': this.$store.state.auth_token,},
      }).then((response) => {
          var jsonData = JSON.parse(JSON.stringify(response.data));

          if (jsonData['status'] == true) {
            Swal.fire({
                  title: 'Success!',
                  text: 'You have been Logged Out Successfully',
                  icon: 'success',
                  confirmButtonText: 'Cool!'
              }).then( () => {
                  // this.$store.store_auth_data({'auth_user': this.username, 'auth_token' : jsonData[]})
                  this.$store.commit('clear_auth_data')

                  window.location.assign('/');
                  // this.$router.push('/');
              });
          }else {
            Swal.fire({
                  title: 'Error!',
                  text: 'Failed to Logout. Please Try Again Later',
                  icon: 'error',
                  confirmButtonText: 'Cool!'
              })
          }
      })
    }

  }

}

</script>

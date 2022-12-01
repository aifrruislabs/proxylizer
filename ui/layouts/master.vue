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
            <li class="nav-item">
              <nuxt-link class="nav-link active" aria-current="page" to="/">Home</nuxt-link>
            </li>
            
          </ul>

          <ul class="navbar-nav navbar-right mb-2 mb-lg-0">
            <li class="nav-item">
              <nuxt-link class="nav-link active" aria-current="page" to="/auth/login">Login</nuxt-link>
            </li>

            <li class="nav-item">
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

export default {

  name: 'Master',
  data() {
    return {
      user: 'Proxy User'
    }
  }

}

</script>

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'proxylizer_ui',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' },
      { rel: 'stylesheet', href: '/bootstrap/css/bootstrap.min.css' },
      { rel: 'stylesheet', href: '/fontawesome/css/fontawesome.min.css' },
      { rel: 'stylesheet', href: '/fontawesome/css/all.min.css' },
      { rel: 'stylesheet', href: '/style/css/demo_3/style.css' },
      { rel: 'stylesheet', href: '/style/css/custom.css' },
      { rel: 'stylesheet', href: '/style/assets/plugin/datatables/responsive.dataTables.min.css' },
      { rel: 'stylesheet', href: '/style/assets/plugin/datatables/dataTables.bootstrap5.min.css' },
    ],
    script: [
      {src: '/style/js/jquery.min.js'},
      {src: '/bootstrap/js/bootstrap.min.js'},
      {src: '/fontawesome/js/fontawesome.min.js'},
      {src: '/style/assets/plugin/jqueryuicalandar/jquery-ui.min.js'},
      {src: '/style/assets/plugin/owlcarousel/owl.carousel.js'},
      {src: '/style/assets/bundles/dataTables.bundle.js'},
    ]
  },

  router: {
    // middleware: ['auth']
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/persistedState.js' },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: '/',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },
  server: {
    host: '0.0.0.0',
    port: 80
  },
}

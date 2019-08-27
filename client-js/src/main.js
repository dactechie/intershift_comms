import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index'
//import VueAuthenticate from 'vue-authenticate'
import axios from 'axios'
import VueAxios from 'vue-axios';
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false


// Vue.axios.defaults.baseURL = 'http://127.0.0.1:5000'
const baseAxios = axios.create({
  baseURL: 'http://127.0.0.1:5000'
})


// Vue.prototype.$http = baseAxios

// Vue.use(VueAuthenticate, {
//   baseUrl: 'http://localhost:5000', // Your API domain
// });
baseAxios.interceptors.response.use(function (response) {
    return response
  }, 
  function (error) {
      console.debug("interceptor error", error)
      store.dispatch('LOGOUT_ACTION')
      router.push('/login')
  
    return Promise.reject(error)
  })

Vue.use(VueAxios, baseAxios)



new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

// router.beforeEach((to, from, next) => {
//     if (to.matched.some(record => record.meta.requiresAuth)) {
//       // this route requires auth, check if logged in
//       // if not, redirect to login page.
//       if (!auth.loggedIn()) {
//         next({
//           path: '/login',
//           query: { redirect: to.fullPath }
//         })
//       } else {
//         next()
//       }
//     } else {
//       next() // make sure to always call next()!
//     }
//   })
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/messages/index'
// import VueAuthenticate from 'vue-authenticate'
import axios from 'axios'
// import VueAxios from 'vue-axios';
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false


// Vue.axios.defaults.baseURL = 'http://127.0.0.1:5000'
const baseAxios = axios.create({
  baseURL: 'http://127.0.0.1:5000'
})
//Vue.use(baseAxios);

Vue.prototype.$http = baseAxios

// Vue.use(VueAuthenticate, {
//   baseUrl: 'http://localhost:5000', // Your API domain
// });

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')


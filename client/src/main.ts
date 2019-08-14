import Vue from 'vue';
import Vuex from 'vuex';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import VueAuthenticate from 'vue-authenticate';
import axios from 'axios';
import VueAxios from 'vue-axios';

import router from './router';
import App from './App.vue';
import { buildStore } from './store/index';

Vue.use(Vuex);
const builtStore = buildStore();

builtStore.replaceState({
    auth: { isLoggedIn: false, userID: '' },
    message: {  messages: [
          {title : 'title',  content : 'content',   created_date : new Date()},
        ]},
});

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

(Vue as any).router = router;

Vue.use(VueAxios, axios);

Vue.use(VueAuthenticate, {
  baseUrl: 'http://localhost:5000', // Your API domain
});


// not working https://github.com/dgrubelic/vue-authenticate/issues/33
// Vue.use(VueAuthenticate, {

//   bindRequestInterceptor: function () {
//     (this as any).$http.interceptors.request.use((config: any) => {
//       console.log('request interceptor')
//       if ((this as any).isAuthenticated()) {
//         config.headers['Authorization'] = [
//           (this as any).options.tokenType, (this as any).getToken()
//         ].join(' ')
//       } else {
//         delete config.headers['Authorization']
//       }
//       return config
//     })
//   },
//   bindResponseInterceptor: function () {
//     (this as any).$http.interceptors.response.use((response: any) => {
//       console.log(response);
//       (this as any).setToken(response)
//       return response
//     })
//   },
// });

const vm  = new Vue({
  router,
  store: builtStore,
  render: (h) => h(App),
}).$mount('#app');

// (vm as any).$auth.isAuthenticated();

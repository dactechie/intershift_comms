import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Logout from './views/Logout.vue';

Vue.use(VueRouter);

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {auth: true},
    },
    {
      path: '/logout',
      name: 'logout',
      component: Logout,
      meta: {auth: true,  redirect: {name: 'default'}},
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {auth: false,  redirect: {name: 'default'}},
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
  ],
});

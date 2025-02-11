import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Logout from './views/Logout.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {requiresAuth: true},
    },
    {
      path: '/logout',
      name: 'logout',
      component: Logout,
      meta: {requiresAuth: true,  redirect: {name: 'default'}},
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {requiresAuth: false,  redirect: {name: 'default'}},
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})

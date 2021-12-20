import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import Register from './views/Register.vue';


Vue.use(Router);

export const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/home',
      component: Home
    },
    {
      path: '/login',
      component: Login
      // component: () => import('./views/Login.vue')
    },
    {
      path: '/register',
      component: Register
      // component: () => import('./views/Register.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      // lazy-loaded
      component: () => import('./views/Profile.vue')
      // component: Profile
    },
    // {
    //   path: '/admin',
    //   name: 'admin',
    //   // lazy-loaded
    //   component: () => import('./views/BoardAdmin.vue')
    //   // component: BoardAdmin
    // },
    // {
    //   path: '/mod',
    //   name: 'moderator',
    //   // lazy-loaded
    //   component: () => import('./views/BoardModerator.vue')
    //   // component: BoardModerator
    // },
    // {
    //   path: '/user',
    //   name: 'user',
    //   // lazy-loaded
    //   component: () => import('./views/BoardUser.vue')
    //   // component: BoardUser
    // }
  ]
});
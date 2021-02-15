import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '@/views/Authenticate/Login'

import Home from '@/views/Home'
import Recipes from '@/views/Recipes'
import ShoppingLists from '@/views/ShoppingLists'
import ShoppingCart from '@/views/ShoppingCart'
import Fridge from '@/views/Fridge'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/recettes',
    name: 'Recipes',
    component: Recipes
  },
  {
    path: '/shopping/listes',
    name: 'ShoppingLists',
    component: ShoppingLists
  },
  {
    path: '/shopping/caddy',
    name: 'ShoppingCart',
    component: ShoppingCart
  },
  {
    path: '/mon-frigo',
    name: 'Fridge',
    component: Fridge
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

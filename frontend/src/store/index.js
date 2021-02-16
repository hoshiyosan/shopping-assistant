import Vue from 'vue'
import Vuex from 'vuex'

// import modules
import auth from './auth'
import accounts from './accounts'
import recipes from './recipes'
import ingredients from './ingredients'
import shoppinglists from './shoppinglists'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    accounts,
    recipes,
    ingredients,
    shoppinglists
  },
  actions: {
    initApp({ dispatch }) {
      dispatch('ingredients/loadUnits', null, { root: true });
    }
  }
})

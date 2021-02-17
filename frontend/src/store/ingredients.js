import { APIObject } from "@/plugins/api"

const unitsAPI = new APIObject("unit", "/ingredients/units");
const categoriesAPI = new APIObject("categories", "/ingredients/categories");
const ingredientsAPI = new APIObject("ingredient", "/ingredients");

export default {
    namespaced: true,
    state: {
        units: [],
        ingredients: null,
        categories: null
    },
    mutations: {
        setUnits(state, units) {
            state.units = [{ name: 'aucune', value: null }, ...units.map(unit => ({ name: unit, value: unit }))];
        },
        setCategories(state, categories) {
            state.categories = [{ name: 'N/A', value: null }, ...categories.map(category => ({ name: category, value: category }))];
        },
        setIngredients(state, ingredients) {
            state.ingredients = ingredients
        }
    },
    actions: {
        loadUnits({ commit }) {
            unitsAPI.search()
                .then(units => commit('setUnits', units))
        },
        loadCategories({ commit }) {
            categoriesAPI.search()
                .then(categories => commit('setCategories', categories))
        },
        loadIngredients({ commit }) {
            return ingredientsAPI.search("").then((ingredients) => {
                commit('setIngredients', ingredients);
                return ingredients;
            })
        },
        get(context, ingredientUID) {
            return ingredientsAPI.get(ingredientUID);
        },
        localSearch({ state }, query) {
            return new Promise(resolve => {
                const regex = new RegExp(query, "i");
                const matches = state.ingredients.filter(ingredient => ingredient.name.match(regex));
                resolve(matches);
            })
        },
        search({ state, dispatch }, query) {
            return new Promise(resolve => {
                // TODO: improve weird caching mechanism
                if (state.ingredients === null) {
                    dispatch('loadIngredients')
                        .then(() => {
                            dispatch('localSearch', query)
                                .then(matches => resolve(matches))
                        })
                } else {
                    dispatch('localSearch', query)
                        .then(matches => resolve(matches))
                }
            })
        },
        create({ dispatch }, ingredientData) {
            return ingredientsAPI.create(ingredientData)
                .then((createdIngredient) => {
                    dispatch('loadIngredients');
                    return createdIngredient
                })
        },
        update({ dispatch }, ingredientData) {
            return ingredientsAPI.update(ingredientData)
                .then((updatedIngredient) => {
                    dispatch('loadIngredients');
                    return updatedIngredient
                })
        },
        delete(context, ingredientUID) {
            return ingredientsAPI.delete(ingredientUID);
        }
    }
}
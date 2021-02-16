import { APIObject } from "@/plugins/api"

const unitsAPI = new APIObject("unit", "/ingredients/units");
const ingredientsAPI = new APIObject("ingredient", "/ingredients");

export default {
    namespaced: true,
    state: {
        units: [],
        ingredients: null
    },
    mutations: {
        setUnits(state, units) {
            state.units = [{ name: 'aucune', value: null }, ...units.map(unit => ({ name: unit, value: unit }))];
        }
    },
    actions: {
        loadUnits({ commit }) {
            unitsAPI.search()
                .then(units => commit('setUnits', units))
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
                    ingredientsAPI.search(query)
                        .then((ingredients) => {
                            state.ingredients = ingredients;
                            dispatch('localSearch', query)
                                .then(matches => resolve(matches))
                        })
                } else {
                    dispatch('localSearch', query)
                        .then(matches => resolve(matches))
                }
            })
        },
        create(context, ingredientData) {
            return ingredientsAPI.create(ingredientData);
        },
        update(context, ingredientData) {
            return ingredientsAPI.update(ingredientData);
        },
        delete(context, ingredientUID) {
            return ingredientsAPI.delete(ingredientUID);
        }
    }
}
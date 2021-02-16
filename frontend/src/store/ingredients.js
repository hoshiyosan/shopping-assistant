import { APIObject } from "@/plugins/api"

const unitsAPI = new APIObject("unit", "/ingredients/units");
const ingredientsAPI = new APIObject("ingredient", "/ingredients");

export default {
    namespaced: true,
    state: {
        units: []
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
        search(context, query) {
            return ingredientsAPI.search(query);
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
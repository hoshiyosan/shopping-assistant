import { APIObject } from '../plugins/api';

const recipesAPI = new APIObject("recipe", "/recipes")

export default {
    namespaced: true,
    actions: {
        get(context, recipeUID) {
            return recipesAPI.get(recipeUID);
        },
        search(context, query) {
            return recipesAPI.search(query);
        },
        create(context, recipeData) {
            return recipesAPI.create(recipeData);
        },
        update(context, recipeData) {
            return recipesAPI.update(recipeData);
        },
        delete(context, recipeUID) {
            return recipesAPI.delete(recipeUID);
        }
    }
}
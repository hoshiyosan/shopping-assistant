import { APIObject } from '../plugins/api';

const recipesAPI = new APIObject("recipe", "/recipes")

function cleanRecipe(recipeData) {
    const recipe = Object.assign({}, recipeData);
    const ingredients = (recipeData.ingredients || []).filter(ingredient => !!ingredient.ingredient_uid);
    recipe.ingredients = ingredients;
    return recipe;
}

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
            return recipesAPI.create(cleanRecipe(recipeData));
        },
        createEmpty({ dispatch }) {
            return dispatch('create', { name: 'Nouvelle recette', diners: 2 });
        },
        update(context, recipeData) {
            return recipesAPI.update(cleanRecipe(recipeData));
        },
        delete(context, recipeUID) {
            return recipesAPI.delete(recipeUID);
        }
    }
}
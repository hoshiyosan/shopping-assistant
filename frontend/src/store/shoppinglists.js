import { APIObject } from '../plugins/api';

const shoppingListsAPI = new APIObject("shoppingList", "/shoppinglists")

export default {
    namespaced: true,
    actions: {
        get(context, shoppingListUID) {
            return shoppingListsAPI.get(shoppingListUID);
        },
        search(context, query) {
            return shoppingListsAPI.search(query);
        },
        create(context, shoppingListData) {
            return shoppingListsAPI.create(shoppingListData);
        },
        createEmpty({ dispatch }) {
            return dispatch('create', { name: 'Nouvelle liste de courses' });
        },
        update(context, shoppingListData) {
            return shoppingListsAPI.update(shoppingListData);
        },
        delete(context, shoppingListUID) {
            return shoppingListsAPI.delete(shoppingListUID);
        },
        addRecipe(context, { shoppingListUID, recipeData }) {
            // load full shopping list object
            return shoppingListsAPI.get(shoppingListUID)
                .then((shoppingList) => {
                    // add recipe to shoppingList object
                    shoppingList.recipes.push(recipeData);
                    console.log(shoppingList)
                    // update object in API
                    shoppingListsAPI.update(shoppingList)
                        .then(() => { return true })
                })
        }
    }
}
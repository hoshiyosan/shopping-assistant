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
        }
    }
}
import { APIObject } from '@/plugins/api'

const accountsAPI = new APIObject("account", "/accounts");


export default {
    namespaced: true,
    state: {
        currentAccount: null
    },
    mutations: {
        setCurrentAccount(state, account) {
            state.currentAccount = account;
        }
    },
    actions: {
        get(context, accountUID) {
            return accountsAPI.get(accountUID);
        },
        search(context, query) {
            return accountsAPI.search(query);
        },
        create(context, accountData) {
            return accountsAPI.create(accountData);
        },
        update(context, accountData) {
            return accountsAPI.update(accountData);
        },
        delete(context, accountUID) {
            return accountsAPI.delete(accountUID);
        }
    }
}
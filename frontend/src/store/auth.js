import http from '@/plugins/http'

const STORED_TOKEN = 'API_KEY';

export default {
    namespaced: true,
    state: {
        authenticated: false
    },
    mutations: {
        setToken(state, token) {
            http.defaults.headers.common['Authorization'] = token ? `Bearer ${token}` : null;
            state.authenticated = token ? true : false;
            if(token){
                localStorage.setItem(STORED_TOKEN, token);
            }else{
                localStorage.removeItem(STORED_TOKEN);
            }
        }
    },
    actions: {
        /**
         * Retrieve access_token from given credentials
         */
        login(context, { email, password }) {
            http.post('/auth/token', { email, password })
                .then(response => {
                    const tokenInfo = response.data;
                    console.log(tokenInfo.access_token);
                })
        },

        /**
         * Try to authenticate from a token previously stored in localStorage
         */
        fromLocalStorage() {
            const token = localStorage.getItem(STORED_TOKEN);
            console.log(token);
        },

        /**
         * Delete credentials from localStorage and app context
         */
        logout({commit}){
            commit('setToken', null);
        }
    },
}
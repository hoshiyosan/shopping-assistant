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
            localStorage.setItem(STORED_TOKEN, token);
            state.authenticated = token ? true : false;
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
        }
    },
}
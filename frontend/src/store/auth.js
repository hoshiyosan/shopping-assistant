import http from '@/plugins/http'

const STORED_TOKEN = 'API_KEY';

export default {
    namespaced: true,
    state: {
        authenticated: false
    },
    mutations: {
        setToken(state, token) {
            if (token) {
                state.authenticated = true;
                http.defaults.headers.common['Authorization'] = `Bearer ${token}`;
                localStorage.setItem(STORED_TOKEN, token);
            } else {
                state.authenticated = false;
                http.defaults.headers.common['Authorization'] = null;
                localStorage.removeItem(STORED_TOKEN);
            }
        }
    },
    actions: {
        /**
         * Validate accessToken
         */
        validateToken({ commit }, accessToken) {
            console.log('validateToken', accessToken)
            return new Promise(resolve => {
                http.get('/accounts/me', { headers: { Authorization: `Bearer ${accessToken}` } })
                    .then((response) => {
                        commit('accounts/setCurrentAccount', response.data, { root: true });
                        resolve(true);
                    })
                    .catch(() => resolve(false));
            })
        },

        /**
         * Retrieve access_token from given credentials
         */
        login({ commit, dispatch }, { email, password }) {
            return new Promise((resolve, reject) => {
                http.post('/auth/token', { email, password })
                    .then(response => {
                        const accessToken = response.data.access_token;
                        dispatch('validateToken', accessToken)
                            .then(success => {
                                if (success) {
                                    commit('setToken', accessToken);
                                    dispatch('initApp', null, { root: true });
                                    resolve("Login succeed!");
                                } else {
                                    reject("Login failed!");
                                }
                            });
                    })
                    .catch(() => reject("Login failed!"));
            })

        },

        /**
         * Try to authenticate from a token previously stored in localStorage
         */
        fromLocalStorage({ commit, dispatch }) {
            return new Promise((resolve, reject) => {
                const accessToken = localStorage.getItem(STORED_TOKEN);
                if (accessToken) {
                    dispatch('validateToken', accessToken)
                        .then(success => {
                            if (success) {
                                commit('setToken', accessToken);
                                dispatch('initApp', null, { root: true });
                                resolve("Login succeed!");
                            } else {
                                reject("Login failed!");
                            }
                        });
                } else {
                    reject("Login failed");
                }
            })
        },

        /**
         * Delete credentials from localStorage and app context
         */
        logout({ commit }) {
            commit('setToken', null);
        }
    },
}
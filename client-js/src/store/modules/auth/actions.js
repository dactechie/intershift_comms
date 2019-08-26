
import Vue from 'vue'

export default  {

    LOGIN_ACTION : async function login({ commit }, creds) {
        try {
            const response = await Vue.axios.post('/auth/login', creds)
            console.log(response)
            commit('setLoggedInUser', { user: creds.username })
            localStorage.setItem('token', response.data.token)

        } catch(err) {
            console.error(err)
        }
    },

    LOGOUT_ACTION : function logout({ commit }) {
        
        commit('setLoggedInUser', { user: null })
        localStorage.removeItem('token')
    },

}
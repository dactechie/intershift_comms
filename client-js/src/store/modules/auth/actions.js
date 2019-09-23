
import Vue from 'vue'

export default  {

    LOGIN_ACTION : async function login({ commit }, creds) {
        try {
            const response = await Vue.axios.post('/auth/login', creds)
            localStorage.setItem('token', await response.data.token)
            localStorage.setItem('user', JSON.stringify(await response.data.user))

            commit('setLoggedInUser',  await response.data.user )

        } catch(err) {
            console.error(err)
        }
    },

    LOGOUT_ACTION : function logout({ commit }) {
        localStorage.removeItem('token')
        localStorage.removeItem('user')
        
        commit('setLoggedInUser', { user: null })
    },

}
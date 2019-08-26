import auth from './modules/auth/'
import messages from './modules/messages/'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    modules:{
        auth,
        messages,
    }
})
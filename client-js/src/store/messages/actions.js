//import shop from '../../api/shop'
import Vue from 'vue'

export default {
    addMessage ({ commit }, text) {
      commit('addMessage', {
        text,
        done: false
      })
    },
  
    removeMessage ({ commit }, message) {
      commit('removeMessage', message)
    },
  
    // togglemessage ({ commit }, message) {
    //   commit('editmessage', { message, done: !message.done })
    // },
  
    editMessage ({ commit }, { message, value }) {
      commit('editMessage', { message, text: value })
    },
  
    LOAD_MESSAGES : async function getMessages ({commit}) {
        try {
          // Vue.axios.defaults.headers.common['Authorization'] =
          //                             'Bearer ' + localStorage.getItem('token');
          const response = await  Vue.prototype.$http.get('/messages',
          {
            headers: {
              'Content-type': 'application/json'
            }
          });        
          // console.log("going to commit", response.data.messages)
          
          commit('updateMessages', response.data.messages)

        } catch(err){
          console.error(err)
        }
      
      
    }
    // toggleAll ({ state, commit }, done) {
    //   state.messages.forEach((message) => {
    //     commit('editmessage', { message, done })
    //   })
    // },
  
    // clearCompleted ({ state, commit }) {
    //   state.messages.filter(message => message.done)
    //     .forEach(message => {
    //       commit('removemessage', message)
    //     })
    // }
  }
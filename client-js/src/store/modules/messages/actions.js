import Vue from 'vue'

export default {

    ADD_MESSAGE : async function addMessage ({ commit }, message) {
      try {
         Vue.axios.defaults.headers.common['Authorization'] =
                                     'Bearer ' + localStorage.getItem('token');
        const response = await  Vue.axios.post('/messages', message)
        // {
        //   headers: {
        //     'Content-type': 'application/json'
        //   }
        // });
        let result = response.data.message
        //console.log("going to commit ", result)
        commit('addMessage', result)

      } catch(err){
        console.error(err)
      }
      
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
          Vue.axios.defaults.headers.common['Authorization'] =
                                       'Bearer ' + localStorage.getItem('token');
          const response = await  Vue.axios.get('/messages',
          {
            headers: {
              'Content-type': 'application/json'
            }
          });        
          //console.log("going to commit", response.data.messages)
          
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
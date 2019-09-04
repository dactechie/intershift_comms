import Vue from 'vue'

export default {

    ADD_MESSAGE : async function addMessage ({ commit }, message) {
      try {
         Vue.axios.defaults.headers.common['Authorization'] =
                                     'Bearer ' + localStorage.getItem('token');
        const response = await  Vue.axios.post('/messags', message)

        let result = response.data.message
        // console.log("going to commit ", result)
        commit('addMessage', result)

      } catch(err){
        console.error(err)
      }      
    },
  
    removeMessage ({ commit }, message) {
      commit('removeMessage', message)
    },
  
    UPDATE_MESSAGE : async function editMessages ({ commit }, message) {
        try {
            Vue.axios.defaults.headers.common['Authorization'] =
                                         'Bearer ' + localStorage.getItem('token');
            const response = await  Vue.axios.put('/messags/'+ message.id, message)
            console.log("update response", response)
    
        } catch(err){
            console.error(err)
      }
      commit('editMessage', message )
    },
  
    LOAD_MESSAGES : async function getMessages ({commit}) {
        try {
            Vue.axios.defaults.headers.common['Authorization'] =
                                       'Bearer ' + localStorage.getItem('token');
            const response = await  Vue.axios.get('/messags');        
          // console.log("going to commit updateMessages", response.data.messages)
          
          commit('updateMessages', response.data.messages)

        } catch(err){
          console.error(err)
        }      
    },

    LOAD_MESSAGE : async function getMessage ({commit}, message_id) {
        try {
            Vue.axios.defaults.headers.common['Authorization'] =
                                       'Bearer ' + localStorage.getItem('token');
          
            const response = await  Vue.axios.get('/messags/'+message_id);         

            commit('setContent', response.data.message)
        } catch(err){
          console.error(err)
        }      
    }

  }
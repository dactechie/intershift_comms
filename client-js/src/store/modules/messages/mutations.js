import Vue from 'vue'
export const STORAGE_KEY = 'messages-vuejs'

// for testing
if (navigator.userAgent.indexOf('PhantomJS') > -1) {
  window.localStorage.clear()
}

export const mutations = {
  addMessage (state, message) {
      state.messages.unshift(message)
  },

  removeMessage (state, message) {
    state.messages.splice(state.messages.indexOf(message), 1)
  },

  editMessage (state,  message) {
    var index = state.messages.findIndex (m=> m.id === message.id);
    if (index !== -1) {
        state.messages[index] = message;
    }

  },
  updateMessages (state, messages) {
      console.log("state", state)
      console.log("messages", messages)
      Vue.set(state, 'messages', messages)
      //state.messages = messages
  },

  setContent(state, message) {
    let mesgIndex = state.messages.findIndex(m =>
        m.id === message.id
    )
    if(mesgIndex > -1) {
        state.messages[mesgIndex]['content'] = message.content
    }
    else
        console.error("did not find message with id ", message.id)
  }
}
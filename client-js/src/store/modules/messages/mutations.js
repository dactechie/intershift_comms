import Vue from 'vue'
export const STORAGE_KEY = 'messages-vuejs'

// for testing
if (navigator.userAgent.indexOf('PhantomJS') > -1) {
  window.localStorage.clear()
}

export const mutations = {
  addMessage (state, message) {
    state.messages.push(message)
  },

  removeMessage (state, message) {
    state.messages.splice(state.messages.indexOf(message), 1)
  },

  editMessage (state, { message, text = message.text, done = message.done }) {
    message.text = text
    message.done = done
  },
  updateMessages (state, messages) {
      console.log("state", state)
      console.log("messages", messages)
      Vue.set(state, 'messages', messages)
      //state.messages = messages
  }
}
export const STORAGE_KEY = 'auth-vuejs'

// for testing
if (navigator.userAgent.indexOf('PhantomJS') > -1) {
  window.localStorage.clear()
}

export const mutations = {
  setLoggedInUser (state, user) {
    state.user = user
  },

//   removeMessage (state, user) {
//     state.user.splice(state.messages.indexOf(message), 1)
//   },

//   editMessage (state, { message, text = message.text, done = message.done }) {
//     message.text = text
//     message.done = done
//   },
//   updateMessages (state, messages) {
//       state.messages = messages
//   }
}
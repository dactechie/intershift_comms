
const getters = {
    load_messages: state => {
            return state.messages
    },
    get_viewing_message: state => {
        return state.viewingMessage
    }
}

export default getters;

import { getStoreBuilder } from 'vuex-typex';
import { MessagesState } from './state';
import { RootState } from '../index';
import { addMessageAction, getMessagesAction, getMesgByIdAction as getMesgByIdAction } from './actions';
import { addMessageMut, clearMessagesMut, fetchedMessagesMut, fullFetchedMessageMut } from './mutations';
import { getById } from './getters';

const initialState: MessagesState = {
    messages: [],
};

const mb = getStoreBuilder<RootState>().module<MessagesState>('message', initialState);
const stateReader = mb.state();
const getFromStoreById = mb.read((state) => getById, 'message');

const MessageManager = {
    // getters + methods
    get state() { return stateReader(); },
    getStoreMesgById(mesgId: number) {
        return getFromStoreById()(stateReader(), mesgId);
    },
    // mutations
    commitAddMessage: mb.commit(addMessageMut),
    commitClearMessages: mb.commit(clearMessagesMut),
    commitFetchedMessages: mb.commit(fetchedMessagesMut),
    commitFullFetchedMessage : mb.commit(fullFetchedMessageMut),

    // actions
    dispatchDelayedAppend: mb.dispatch(addMessageAction),
    dispatchGetMessages : mb.dispatch(getMessagesAction),
    dispatchGetMessage : mb.dispatch(getMesgByIdAction),
};

export default MessageManager;
export { mb as MessageModuleBuilder };




// const getMessageById= mb.read((state) => (state: MessagesState, mesg_id: number) => {
//   getMesgById(state, mesg_id);
// }, "message");

// const oldestNameGetter = mb.read((state): string | undefined =>
// {
//     const oldestMessage = (<Message[]>state.messages).slice().sort((a, b) => a.dob.getTime() - b.dob.getTime())[0]
//     return oldestMessage && oldestMessage.name
// }, "oldestName")

// const dateOfBirthForMethod = mb.read((state) => (name: string) =>
// {
//     const matches = state.messages.filter(b => b.name === name)
//     if (matches.length)
//     {
//         return matches[0].dob
//     }

//     return
// }, "dob")


    // get oldestName() { return oldestNameGetter() },
    // dateOfBirthFor(name: string) { return dateOfBirthForMethod()(name) },

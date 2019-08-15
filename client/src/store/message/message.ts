import { getStoreBuilder } from 'vuex-typex';
import { MessagesState, IMessage } from './state';
import { RootState } from '../index';
import { addMessageAction, getMessagesAction, getMesgById } from './actions';
import { addMessageMut, clearMessagesMut, fetchedMessagesMut, fullFetchedMessageMut } from './mutations';
import { getBasicMesgById } from './getters';

const initialState: MessagesState = {
    messages: [],    
};

const mb = getStoreBuilder<RootState>().module<MessagesState>('message', initialState);

const _getBMessageById= mb.read((state) => getBasicMesgById, "message"); //(state: MessagesState, mesg_id: number)
// const getMessages= mb.read((state) => getMesgs, "message"); //(state: MessagesState, mesg_id: number)

const stateReader = mb.state();

const MessageManager = {
    // getters + methods
    get state() { return stateReader(); },
    //getById(mesg_id: number) { return getMessageById()(stateReader(), mesg_id); },
    _getBMesgById(mesg_id: number) { return _getBMessageById()(stateReader(), mesg_id); },

    // mutations
    commitAddMessage: mb.commit(addMessageMut),
    commitClearMessages: mb.commit(clearMessagesMut),
    commitFetchedMessages: mb.commit(fetchedMessagesMut),
    commitFullFetchedMessage : mb.commit(fullFetchedMessageMut),

    // actions
    dispatchDelayedAppend: mb.dispatch(addMessageAction),
    dispatchGetMessages : mb.dispatch(getMessagesAction),
    dispatchGetMessage : mb.dispatch(getMesgById),
};

// Message.commitAddMessage({ Message: { created_date: new Date(1980, 2, 3), title: "Louise" } })

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

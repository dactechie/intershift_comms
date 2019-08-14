import { getStoreBuilder } from 'vuex-typex';
import { MessagesState, IMessage } from './state';
import { RootState } from '../index';
import addMessageAction from './actions/addAfterDelay';

const initialState: MessagesState = {
    messages: [],
};

const mb = getStoreBuilder<RootState>().module<MessagesState>('Message', initialState);

const addMessageMut = (state: MessagesState, payload: { Message: IMessage }) => state.messages.push(payload.Message);
const removeFirstMessageMut = (state: MessagesState) => state.messages.shift();
const clearMessagesMut = (state: MessagesState) => state.messages = [];

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

const stateReader = mb.state();

const MessageManager = {
    // getters + methods
    get state() { return stateReader(); },
    // get oldestName() { return oldestNameGetter() },
    // dateOfBirthFor(name: string) { return dateOfBirthForMethod()(name) },

    // mutations
    commitAddMessage: mb.commit(addMessageMut),
    commitRemoveFirstMessage: mb.commit(removeFirstMessageMut),
    commitClearMessages: mb.commit(clearMessagesMut),

    // actions
  //  dispatchRemoveFirstAfterDelay: mb.dispatch(removeFirstAfterDelay),

    dispatchDelayedAppend: mb.dispatch(addMessageAction),
};

// Message.commitAddMessage({ Message: { created_date: new Date(1980, 2, 3), title: "Louise" } })
// Message.commitRemoveFirstMessage()
// Message.dateOfBirthFor("Louise")
// Message.dispatchRemoveFirstAfter(1000)
// let m:IMessage = {
//     id:1,
//     title: 'cool',
//     created_username: 'aftab',
//     created_date: new Date(),
//     read_by: 'aftab',
// };

// Message.dispatchDelayedAppend(m);

export default MessageManager;
export { mb as MessageModuleBuilder };

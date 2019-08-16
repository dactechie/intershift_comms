import { BareActionContext } from 'vuex-typex';
import MessageManager from './message';
import { IMessage, MessagesState } from './state';
import { RootState } from '../index';
import Vue from 'vue';

export async function
    addMessageAction(context: BareActionContext<MessagesState, RootState>, message: IMessage) {

    const path = '/messages';
    const res = await Vue.axios.post(path, message);
    if (await res.data != null) {
        const addedMessage: IMessage =  res.data.message as IMessage;
        MessageManager.commitAddMessage({ Message: addedMessage});
    }
    return;
}

export async function
    getMessagesAction(context: BareActionContext<MessagesState, RootState>) {

    const path = '/messages';
    Vue.axios.defaults.headers.common['Authorization'] =
                                'Bearer ' + localStorage.getItem('token');
    const res = await Vue.axios.get(path);
    if (await res.data != null) {
        const messages: IMessage[] = res.data.messages as IMessage[];
        MessageManager.commitFetchedMessages({ Messages: messages});
    }
    return;
}


export async function getMesgByIdAction(
    context: BareActionContext<MessagesState, RootState>, messageId: number):
    Promise<IMessage | undefined> {

    const bMesg  = await MessageManager.getStoreMesgById(messageId);
    if (!bMesg) {
        return undefined;
    }
    const path = '/messages/' + messageId;
    Vue.axios.defaults.headers.common['Authorization'] =
                               'Bearer ' + localStorage.getItem('token');
    const res = await Vue.axios.get(path);

    if (await res.data != null) {
        const message: IMessage = res.data.message as IMessage;
        MessageManager.commitFullFetchedMessage({ Message: message});
    }
  }

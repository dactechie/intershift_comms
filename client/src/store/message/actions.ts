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
        MessageManager.commitAddMessage({ Message: message});
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
        let messages:IMessage[] = <IMessage[]> res.data.messages;
        MessageManager.commitFetchedMessages({ Messages: messages});
    }
    return;
}


export async function getMesgById 
    (context: BareActionContext<MessagesState, RootState>, mesg_id: number):
     Promise<IMessage | undefined> {
    
    const bMesg  = await MessageManager._getBMesgById(mesg_id);

    if (!bMesg){
        return undefined;
    }
    const path = '/messages/' + mesg_id;
    Vue.axios.defaults.headers.common['Authorization'] =
                               'Bearer ' + localStorage.getItem('token');
    const res = await Vue.axios.get(path);
    
    if (await res.data != null) {
        let message:IMessage =<IMessage>  res.data.message;
        MessageManager.commitFullFetchedMessage({ Message: message});        
    }
  }

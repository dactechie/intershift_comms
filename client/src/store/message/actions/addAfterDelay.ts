import { BareActionContext } from 'vuex-typex';
import MessageManager from '../message';
import { IMessage, MessagesState } from '../state';
import { RootState } from '../../index';
import Vue from 'vue';

export default async function addAsync(context: BareActionContext<MessagesState, RootState>, message: IMessage) {
   // const addMessageAction = async (context: BareActionContext<MessagesState, RootState>) =>
   // {
     //   await MessageService.addMessage(message);
    const path = 'http://localhost:5000/messages';
    const res = await Vue.axios.post(path, message);
    if (res.data != null) {
        MessageManager.commitAddMessage({ Message: message});
    }
    //    .then(() => {
    //      // this.fetchMessages();
    //        this.$emit('savedMessage');
    //    })
    //    .catch((error) => {
    //      // eslint-disable-next-line
    //      alert('error ' + error);
    //      // console.log(error);
    //      // this.fetchMessages();
    //    });
   // }

    // if (context.state.messages.length > 2)
    // {
    //     await new Promise((resolve, _) => setTimeout(resolve, delay)); // second delay
    //     //message.commitAddMessage()
    // }

    return;
}

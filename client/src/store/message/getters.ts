
import { IMessage, MessagesState } from './state';

export async function getById(
    state: MessagesState, messageId: number): Promise<IMessage | undefined> {
    const basicMessage: IMessage | undefined = state.messages.find( (mesg) => {
        return mesg.id === messageId;
    });
    return basicMessage;
  }

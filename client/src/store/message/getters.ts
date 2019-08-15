
import { IMessage, MessagesState } from './state';

export async function getBasicMesgById 
    (state: MessagesState, mesg_id: number): Promise<IMessage | undefined> {
    
    const basicMessage:IMessage | undefined = state.messages.find( mesg => {
        return mesg.id == mesg_id;
    });

    return basicMessage;
  }
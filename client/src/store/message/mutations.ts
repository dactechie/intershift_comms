
import { IMessage, MessagesState } from './state';

export const addMessageMut = (state: MessagesState, payload: { Message: IMessage }) =>
                                 state.messages.unshift(payload.Message);

export const clearMessagesMut = (state: MessagesState) => state.messages = [];

export const fetchedMessagesMut = (state: MessagesState , payload: { Messages: IMessage[] }) =>
                                 state.messages = payload.Messages;

export const fullFetchedMessageMut = (state: MessagesState, payload: { Message: IMessage }) => {
        state.messages.forEach((m) => {
                if (m.id === payload.Message.id) {
                    m.content = payload.Message.content;
                    return;
                }
        });
};


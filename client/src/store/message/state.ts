export interface IMessage {
    id?: number;
    title: string;
    content?: string;
    created_username?: string;
    created_date: Date;
    read_by?: string[];
}

export interface MessagesState {
    messages: IMessage[];
}

export interface IMessage {
    id?: number;
    title: string;
    content?: string;
    created_username?: string;
    created_date: Date;
    read_by?: string[];
    update_date?: Date;
}

export interface MessagesState {
    messages: IMessage[];
}

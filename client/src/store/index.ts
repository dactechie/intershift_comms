// import Vue from 'vue';
// import Vuex, {Store} from 'vuex';
// import { messages } from '@/store/Messages';
// import { State, Message } from '@/types';
// import { mutations } from './mutations';
// import actions from './actions';
import { getStoreBuilder } from 'vuex-typex';
import { AuthState } from './auth/state';
import { MessagesState } from './message/state';
// import message from './message/message'
// import plugins from './plugins'

// Vue.use(Vuex);

export interface RootState {
    auth: AuthState;
    message: MessagesState;
}

export const buildStore = () => getStoreBuilder<RootState>().vuexStore();

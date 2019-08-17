// import Vuex from 'vuex'
// import { ModuleBuilder } from 'vuex-typex'
// import { Module } from 'vuex'
import { AuthState } from './state';
import { RootState } from '../index';
import { getStoreBuilder } from 'vuex-typex';
import { loginAction } from './actions';
import { getUsername} from './getters';

const initialState: AuthState = {
    username: 'INITIAL_STATE',
    isLoggedIn: true,
};

const moduleBuilder = getStoreBuilder<RootState>().module<AuthState>('auth', initialState);
const stateReader = moduleBuilder.state();
const getUser = moduleBuilder.read((state) => getUsername, 'getUsername');
const auth = {
    get state() { return stateReader(); },
    getLoggedInUser() {
        return getUser()(this.state);
    },
    commitSetUsername: moduleBuilder.commit((state, payload: { username: string }) =>
                        // console.log("sdf", payload.username);
                        state.username = payload.username, 'setUsername'),
    commitSetIsLoggedIn: moduleBuilder.commit((state, payload: { isLoggedIn: boolean }) =>
                        state.isLoggedIn = payload.isLoggedIn, 'isLoggedIn'),
    dispatchLogin: moduleBuilder.dispatch(loginAction),
};

export default auth;

import { BareActionContext } from 'vuex-typex';
import { AuthState, IAuthCredentials } from './state';
import AuthManager from './auth';
import { RootState } from '../index';
import Vue from 'vue';
import auth from './auth';

export async function
    loginAction(context: BareActionContext<AuthState, RootState>, creds: IAuthCredentials) {
    // context.state.isLoggedIn -> if one user is logged in, log them out.
    // context.rootState.
        AuthManager.commitSetIsLoggedIn({isLoggedIn: true});
        AuthManager.commitSetUsername({username: creds.username});

        // auth.state.username
        localStorage.setItem('token', creds.token);
        // console.log('LoginAction Root state ' , context.rootState.auth.username);

}

<template>
    <div>
        <h1>Login</h1>
        <hr/>

        <form @submit.prevent="login()">
            <table><tr>
                <td>Email:</td>
                <td><input v-model="email" /></td>
            </tr><tr>
                <td>Password:</td>
                <td><input v-model="password" type="password" /></td>
            </tr>
            <!-- <tr>
                <td></td>
                <td><label><input v-model="data.rememberMe" type="checkbox" /> Remember Me</label></td>
            </tr> -->
            <!-- <tr>
                <td></td>
                <td><label><input v-model="data.fetchUser" type="checkbox" /> Fetch User (test)</label></td>
            </tr> -->
            <tr>
                <td></td>
                <td><button type="submit">Login</button></td>
            </tr></table>

            <hr/>

            <!-- <div v-show="error" style="color:red; word-wrap:break-word;">{{ error | json }}</div> -->
        </form>
    </div>
</template>

<script lang="ts">

import Vue from 'vue';
import Component from 'vue-class-component';
import AuthManager from '../store/auth/auth';
import { IAuthCredentials } from '../store/auth/state';

@Component ({
  name: 'Login',
})
export default class Login extends Vue {
    private email: string = '';
    // private username: string ='';
    private password: string = '';
    private context: string = 'login context';
    private error = null;

    private login() {
        (this as any).$auth
            .login({ email: this.email,
                     password : this.password })
            .then((response: any)  => {
                AuthManager.dispatchLogin(       {
                        username: this.email,
                        password: '',
                        token:  response.data.token,
                    } as IAuthCredentials);
            })
            .then(() => {
                // localStorage.setItem('token', response.data.token);
                this.$router.push('/');
            });
        // Execute application logic after successful login
    }
}

</script>

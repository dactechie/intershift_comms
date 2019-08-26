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
            <tr>
                <td></td>
                <td><button type="submit">Login</button></td>
            </tr></table>

            <hr/>

            <!-- <div v-show="error" style="color:red; word-wrap:break-word;">{{ error | json }}</div> -->
        </form>
    </div>
</template>

<script lang="js">

// import AuthManager from '../store/auth/auth';

export default {

    data() {
        return {
            email : '',
            password : '',
            context : 'login context',
            error : null,
        }
    },

    methods: {

        login: function() {
            console.log(this.email)
            this.$store.dispatch('LOGIN_ACTION', {
                username: this.email,
                password: this.password,
            })

            //     .then(() => {
            //         // localStorage.setItem('token', response.data.token);
            //         this.$router.push('/');
            //     });
            // Execute application logic after successful login
        }
    }
}

</script>

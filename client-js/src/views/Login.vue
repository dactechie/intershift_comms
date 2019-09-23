<template>
    <form @submit.prevent="login()">
        <LoginCharacter>
            <template v-slot:loginField>
                <input id="loginEmail" type="text" class="email" required maxlength="254" />
            </template>
            <template v-slot:passwordField>
                <input type="password" id="loginPassword" required />
            </template>
            <template v-slot:showPasswordField>
                <input id="showPasswordCheck" type="checkbox"/>
            </template>
            <template v-slot:submitButton>
                <button id="login" type="submit">Log in</button>
            </template>
        </LoginCharacter>
    </form>
</template>


<script lang="js" scoped>

import LoginCharacter from '@/components/LoginCharacter'; 

export default {
    components: {
      LoginCharacter,
    },
    data() {
        return {
          error: null,
          email: null,
          password: null,
        }
    },
    mounted() {
      this.email=document.querySelector('#loginEmail'),
      this.password=document.querySelector('#loginPassword')
    },
    methods: {
      login: function() {            
          this.$store.dispatch('LOGIN_ACTION', {
              username: this.email.value ,
              password: this.password.value, 
          }).then((result) => {
              this.$router.push('/')
          })
      },
    }
}

</script>

<style lang="scss" scoped>

    @import '@/assets/sass/variables.scss';

    form {
        position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%);
        display: block; width: 100%; max-width: 400px; background-color: #FFF;
        margin: 0; padding: 2.25em; box-sizing: border-box; border: solid 1px #DDD; border-radius: .5em;
        font-family: 'Source Sans Pro', sans-serif;
    }
    input[type="text"], input[type="password"] {
		display: block; margin: 0; padding: 0 1em 0; padding: .875em 1em 0;
		background-color: $inputBG; border: solid 2px $darkBlue; border-radius: 4px; -webkit-appearance: none;
		box-sizing: border-box;
		width: 100%; height: 65px;
		font-size: 1.55em; color: #353538; font-weight: 600; font-family: inherit;
		transition: box-shadow .2s linear, border-color .25s ease-out;
		&:focus {
			outline: none;
			box-shadow: 0px 2px 10px rgba(0,0,0,.1);
			border: solid 2px $medBlue;
		}
	}
	button {
		display: block; margin: 0; padding: .65em 1em 1em;
		background-color: $medBlue; border: none; border-radius: 4px;
		box-sizing: border-box; box-shadow: none;
		width: 100%; height: 65px;
		font-size: 1.55em; color: #FFF; font-weight: 600; font-family: inherit;
		transition: background-color .2s ease-out;
		&:hover, &:active {
			background-color: $darkBlue;
		}
    }
    
</style>
<template>
    <div>
        <h1> You have been logged out </h1>

    </div>
</template>

<script lang="js">

import AuthManager from '../store/modules/auth'
export default {
    mounted() {
        AuthManager.dispatchLogout()
        this.$router.push('/login')
    }
}

</script>

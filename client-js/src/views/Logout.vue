<template>
    <div>
        <h1> You have been logged out </h1>

    </div>
</template>

<script lang="js">

import {  mapActions } from 'vuex'

export default {
    mounted() {
        this.LOGOUT_ACTION()
        this.$router.push('/login')
    },
    methods:{
        ...mapActions([
            'LOGOUT_ACTION',
        ]),
    }
}

</script>

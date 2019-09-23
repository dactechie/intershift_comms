<template>
    <div>
        <h1> You have been logged out </h1>

    </div>
</template>

<script lang="js">

import {  mapActions } from 'vuex'

export default {
    methods:{
        ...mapActions([
            'LOGOUT_ACTION',
        ]),
    },
    mounted() {
        this.LOGOUT_ACTION()
        this.$router.push('/login')
    },
}

</script>

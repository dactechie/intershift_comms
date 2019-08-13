<template>
    <div>
        <h1> You have been logged out </h1>

    </div>
</template>

<script lang="ts">

import Vue from 'vue';
import Component from 'vue-class-component';

@Component ({
  name: 'Logout',
})
export default class Logout extends Vue {
    private mounted() {
        localStorage.removeItem ('token');
        this.$router.push('/');
    }
}

</script>

<template>
  <div class="home">
    <!-- <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/> -->
    <Messages/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
// import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
import Messages from '@/components/Messages.vue';

@Component({
  components: {
  //  HelloWorld,
    Messages,
  },
})
export default class Home extends Vue {}
</script>

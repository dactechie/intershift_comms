<template>
  <div class="home">
    <!-- <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/> -->
    <MessagesComp/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
// import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
import MessagesComp from '@/components/MessagesComp.vue';

@Component({
  components: {
  //  HelloWorld,
    MessagesComp,
  },
})
export default class Home extends Vue {}
</script>

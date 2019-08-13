<template>
  <div class="home">
    <MessagesComp/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import MessagesComp from '@/components/MessagesComp.vue';

@Component({
  components: {
    MessagesComp,
  },
})
export default class Home extends Vue {}
</script>

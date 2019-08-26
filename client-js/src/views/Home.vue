<template>
  <MessagesTItems />

</template>

<script>
import MessagesTItems from '../components/MessagesTItems.vue'

export default {
  components: {
    MessagesTItems,
  },
  mounted() {
      console.log("mounted ")
      //this.$router.push('/login');
  }
};
</script>

<template>
   <v-app id="inspire">

    
    <AppBar  v-if="this.$route.path !== '/login'"/>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <router-view></router-view>
        </v-row>
      </v-container>
    </v-content>

      <AddMessage 
       v-if="this.$route.path !== '/login'"
       @addedMessage="showSuccess = true" />

        <v-snackbar
            v-model="showSuccess"
            :timeout="2000"
            bottom
            color="success"
            >
            New message added by you
            <v-btn text color="white" @click="showSuccess=false">Close</v-btn>
        </v-snackbar>
  </v-app>
</template>

<script>
import AppBar from './components/AppBar'
import AddMessage from './components/AddMessage';

export default {
    name: 'App',
    components: {
        AppBar,
        AddMessage,
    },
    props: {
      source: String,
    },
    data: () => ({
      dialog: false,
      showSuccess: false,
    }),
    // mounted() {
    //     console.log(this.$route.path)
    // }
  }
</script>

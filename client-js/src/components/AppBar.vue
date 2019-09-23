<template>
        <v-app-bar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      app
      color="light-blue lighten-2"
      dark
    >
      <v-toolbar-title
        style="width: 300px"
        class="ml-0 pl-4"
      >
        <span class="hidden-sm-and-down">Arcadia Handover notes</span>
      </v-toolbar-title>
      <!-- <SearchBar/> -->
      <v-text-field
        flat
        solo-inverted
        hide-details
        label="Search"
        class="hidden-sm-and-down"
      ></v-text-field>
      <v-spacer></v-spacer>
      
      <a v-if="getLoggedInUser.admin" :href="admin_url">Admin </a> &nbsp;
      
      <!-- <v-btn icon> -->
          <!-- <img :src="avatar_src"
                :alt="getLoggedInUser.username"/> -->
        <!-- <v-avatar color="getLoggedInUser.color" slot="icon" :size="40">
            <span class="white--text headline">{{getLoggedInUser.initials}}</span>
        </v-avatar>
-->
        <img :src="avatar_src" height="40px" width="40px"
                :alt="getLoggedInUser.username"/> 
     

        <v-btn icon to="/logout">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>
</template>

<script>

import {ADMIN_URL} from '@/constants'
// import SearchBar from '@/components/SearchBar'
import { mapGetters } from 'vuex'
export default {
    components: {
        // SearchBar,
    },
    data: ()=>({
        admin_url: ADMIN_URL,
        avatar_src:'',
        
    }),
    computed: {
        ...mapGetters([
            'getLoggedInUser',      // TODO check this .,.when i log out and log in the avatar remains the same till I refresh the page !!
        ]),
        
    },
    mounted() {
        // {"admin":true,"color":"blue","initials":"MJ","public_id":"fc4d703b-3ff5-465f-87ae-0a2b29f5d0d1","username":"aftab.jalal"}
        if (!this.getLoggedInUser) {
            // reload
            console.log("get logged in user was null,... reloading....")
            this.$router.push('/');
        }
        this.avatar_src = require('../assets/images/avatars/' + this.getLoggedInUser.username + '.svg')
        // this.$refs.avatar.title =  this.getLoggedInUser.initials
    },
}
</script>
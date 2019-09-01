<template>
   <v-app id="inspire">

    <AppBar />

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

      <AddMessage />

   
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
    
      /*items: [
        { icon: 'contacts', text: 'Contacts' },
        // { icon: 'history', text: 'Frequently contacted' },
        // { icon: 'content_copy', text: 'Duplicates' },
        // {
        //   icon: 'keyboard_arrow_up',
        //   'icon-alt': 'keyboard_arrow_down',
        //   text: 'Labels',
        //   model: true,
        //   children: [
        //     { icon: 'add', text: 'Create label' },
        //   ],
        // },
        // {
        //   icon: 'keyboard_arrow_up',
        //   'icon-alt': 'keyboard_arrow_down',
        //   text: 'More',
        //   model: false,
        //   children: [
        //     { text: 'Import' },
        //     { text: 'Export' },
        //     { text: 'Print' },
        //     { text: 'Undo changes' },
        //     { text: 'Other contacts' },
        //   ],
        // },
        { icon: 'settings', text: 'Settings' },
//         { icon: 'chat_bubble', text: 'Send feedback' },
        { icon: 'help', text: 'Help' },
                
      ],*/
    }),
  }
</script>

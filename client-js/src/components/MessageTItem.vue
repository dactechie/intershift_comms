<template>
  <v-timeline-item
        fill-dot 
        v-bind:color="message.created_user.color"
        large
        >
        <v-avatar slot="icon">
          <img ref="avatar" 
                :alt="message.created_user.username"/>
        </v-avatar>
        <span slot="opposite"><div class="grey--text">{{message.created_user.username | properFirstname }}</div></span>
        <v-container >
        <v-card  class="mx-auto"  >
   
            <v-layout row class="pl-6">
                <v-flex xs10 class="mt-1">
                    <v-card-title class="headline-2"> {{message.title}} </v-card-title>
                    <div class="flex-grow-1"></div>
                </v-flex>
                <v-flex xs2 v-if="message.with_action" class="mt-3 pr-1">
                    <div v-if="message.actioned_by" >
                        <v-icon class="success">mdi-check-bold</v-icon>
            
                    </div>
                    <div v-else class="tooltip">
                        <span class="tooltiptext">Requires action</span>
                        <v-icon class="warning">mdi-hazard-lights</v-icon>
                    </div>
                </v-flex>
            </v-layout>
       
            <v-layout row wrap class="pl-3 ml-4">                
                <v-flex xs12>
                    <div class="caption grey--text"> {{message.created_date| friendlyDate}} </div>
                </v-flex>

            </v-layout>
            <v-layout row wrap class="my-3 pl-3 ml-4"> 
                <v-flex xs12>
                    <ReadByUserBadges :read_by_list="message.read_by"/>
                </v-flex>
            </v-layout>
            <v-divider></v-divider>
  
            <v-card-actions :class="seenByMe">
                <v-btn @click="showMessage" text>Read Message</v-btn>
                <ViewMessage :message="message" @closeViewer="updateMessage" v-if="dialog"/>
            </v-card-actions>
        </v-card>
        </v-container>

  </v-timeline-item>
</template>

<script>

import ViewMessage from './ViewMessage'
import ReadByUserBadges from './ReadByUserBadges'
import { friendlyDate } from '../filters/date-formatters'
import { properFirstname } from '../filters/string-formatters'
import { mapGetters } from 'vuex'

export default {
    components:{
        ViewMessage,
        ReadByUserBadges
    },
    filters: {
        friendlyDate,
        properFirstname,
    },
    props : ["message"],
    
    data: () => ({
        dialog: false,
        value: true,
    }),
    computed: {
        ...mapGetters([
            'getLoggedInUser',
        ]),
      seenByMe() {
         return this.message['read_by_me'] ? 'seen' : 'new';
      }
    },
    mounted() {
        this.$nextTick(function () {
            this.$refs.avatar.src = require('../assets/images/avatars/' + this.message.created_user.username + '.svg')
            this.$refs.avatar.title =  this.message.created_user.initials
        })
    },
    methods: {
        showMessage() {
                if (!this.message.read_by.some( (el)=> el.username === this.getLoggedInUser.username)) {
                    this.message.read_by.push(this.getLoggedInUser)
                }
                this.message['read_by_me'] ='seen'
                this.dialog = true
        },
        updateMessage(message) {
            this.dialog = false
            this.message.read_by = message['read_by']
            if (message['actioned_by'] && this.message['with_action']) {
                this.message['actioned_by'] = message['actioned_by']
            }            
        },
    },
  }
</script>

<style scoped>

.new {
    font-weight: bold;
    background-color: tomato;
}
.seen {
    font-weight: normal;
}

/* Tooltip container */
.tooltip {
  position: relative;
  display: inline-block;
}

/* Tooltip text */
.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
  background-color: black;
  color: #fff;
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;
 
  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
}

/* Show the tooltip text when you mouse over the tooltip container */
.tooltip:hover .tooltiptext {
  visibility: visible;
}

</style>
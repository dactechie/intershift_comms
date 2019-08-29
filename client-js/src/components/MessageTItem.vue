<template>
  <v-timeline-item
        fill-dot 
        color="orange"
        large
        >
        <template v-slot:icon>
            <span class="white--text sm-1">{{message.created_username}}</span>
        </template>
        <v-row class="pt-1">
           
            <v-col cols="3">
              <small>{{message.created_date| friendlyDate}} </small>
            </v-col>
            <v-col>
                
                     <div :class="seenByMe"> 
                         <v-btn @click="showMessage" >
                              {{message.title}} </v-btn>
                         <!-- <v-btn @click="showMessage"> {{message.title}} </v-btn> -->
                        <ViewMessage :message="message" @closeViewer="updateMessage" v-if="dialog"/>
                  
                <div v-if="message.with_action" >
                    <div v-if="message.actioned_by" >
                        Actioned by: {{ message.actioned_by }}
                    </div>
                    <div v-else>
                        ! Requires Action !
                    </div>
                    
                </div>
              <div class="caption">Read by: {{message.read_by}}</div>
                </div> 
            </v-col>
           
        </v-row>
  </v-timeline-item>
  
    <!-- <v-timeline-item
        fill-dot
        class="white--text mb-12"
        color="orange"
        large
      >
            <template v-slot:icon>
                <span>JL</span>
            </template>

            <v-text-field
                v-model="input"
                hide-details
                flat
                label="Leave a comment..."
                solo
                @keydown.enter="comment"
                >
                <template v-slot:append>
                    <v-btn
                    class="mx-0"
                    depressed
                    @click="comment"
                    >
                    Post
                    </v-btn>
                </template>
            </v-text-field>

    </v-timeline-item> -->
</template>

<script>

import ViewMessage from './ViewMessage'
import { friendlyDate } from '../filters/date-formatters'
//import { mapActions } from 'vuex'

export default {
    components:{
        ViewMessage
    },
    filters: {
        friendlyDate,
    //    seenByMe,
    },
    props : ["message"],
    
    data: () => ({
        dialog: false,
    }),
    computed: {
      seenByMe() {
         return this.message['read_by_me'] ? 'seen' : 'new';
      }
    },
    methods: {
        // ...mapActions([
        //     'LOAD_MESSAGE',
        // ]),
        showMessage() {
                this.message['read_by_me'] ='seen'
                this.message.read_by = 'me'
                this.dialog = true
        },
        updateMessage(message) {
            this.dialog = false
            this.message.read_by = message['read_by']
            if (message['actioned_by'] && this.message['with_action']) {
                this.message['actioned_by'] = message['actioned_by']
            }
            
        }

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
</style>
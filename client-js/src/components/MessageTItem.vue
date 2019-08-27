<template>
  <v-timeline-item
        fill-dot 
        color="orange"
        large
        >
        <template v-slot:icon>
            <span class="white--text sm-1">{{message.created_username[0]}}</span>
        </template>
        <v-row class="pt-1">
           
            <v-col cols="3">
              <small>{{message.created_date| friendlyDate}} </small>
            </v-col>
            <v-col>
                
                     <div :class="seenByMe">{{message.title}}
                        <!-- <ViewMessage  :message_id="message.id" :title="message.title"/> -->
                    </div> 
                
              <div class="caption">Read by: {{message.read_by}}</div>
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
    mounted(){
        console.log("in comp", this.message)  
    },
    methods: {
    },
  }
</script>

<style scoped>

.new {
    font-weight: bold;
}
.seen {
    font-weight: normal;
}
</style>
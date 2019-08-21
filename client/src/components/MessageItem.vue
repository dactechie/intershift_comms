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
              <div :class="seenByMe">{{message.title}}</div>
              <div class="caption">Read by: {{message.read_by}}</div>
            </v-col>
        </v-row>
  </v-timeline-item>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
import { friendlyDate } from '../filters/date-formatters';
import { IMessage } from '../store/message/state';

@Component({
    name: 'MessageItem',
    filters: {
        friendlyDate,
    },
    computed :{
        seenByMe() {
            return this.message['read_by_me'] ? 'seen' : 'new';        
    }},
})
export default class MessageItem extends Vue {
    @Prop({type: Object as () => IMessage}) 
    public message!: IMessage;
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
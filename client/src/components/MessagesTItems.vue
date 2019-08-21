<template>

            <v-timeline :dense="$vuetify.breakpoint.smAndDown">
                
                <MessageItem v-for="m in messages" :message="m" :key="m.id" />
                
            </v-timeline>
           


</template>

<script lang="ts">

import Vue from 'vue';
import Component from 'vue-class-component';
import MessageItem from '@/components/MessageItem.vue';
import MessageManager from '../store/message/message';
import AuthManager from '../store/auth/auth';
import { IMessage } from '../store/message/state';


@Component({
    name: 'MessagesTItems',
    components: {
        MessageItem,
    },
})
export default class MessagesTItems extends Vue {
    private message: any;
    private showMessage: boolean =  false;
    private addNew: boolean = false;

    public mounted() {
      this.fetchMessages();
    }

    get messages() {
        return MessageManager.state.messages;
    }

    private openMessage(id: number) {
        // this fetches it and commits it to the store.
        MessageManager.dispatchGetMessage(id).then( (res) => {
            // now get it from the store
            MessageManager.getStoreMesgById(id).then((r) => {
                this.message = r;
                // this.message['isNew'] = '';
                alert(this.message.content);
                this.showMessage = true;
            });
        });

    }
    private addedMessage() {
        // alert('cool');
    }
    private toggleAddMessage() {
        this.addNew = !this.addNew;
    }
    private fetchMessages() {
        MessageManager.dispatchGetMessages().then((response) => {
            // console.log(MessageManager.state.messages);
        });
    }
}

</script>

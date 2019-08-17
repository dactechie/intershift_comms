<template>
 <div id="app">
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
            <h1>Messages</h1>
            <hr><br><br>
            <!-- <alert :message="message" v-if="showMessage"></alert> -->
            <!-- <button type="button" class="btn btn-success btn-sm" v-b-modal.Message-modal>Add Message</button> -->
            <button type="button" class="btn btn-success btn-sm" @click.prevent="toggleAddMessage">Add Message</button>
            <br><br>
            <AddMessage @added_message="addedMessage" v-if="addNew"/>
            <br><br>
            <ViewMessage :message=message v-if="showMessage"/>
            <table class="table table-hover">
                <thead>
                    <tr>
                            
                    <th scope="col">Created by</th>
                    <th scope="col">Title</th>
                    <th scope="col">Create date</th>
                    <th scope="col">Read by</th>
                    <!-- <th scope="col">Read?</th> -->
                    <th></th>
                    </tr>
                </thead>
                <tbody> 
                     <!-- :class="article.isSeenByMe" -->
                <tr v-for="article in messages" :key="article.id" :class="article.read_by | seenByMe">
                    <td>{{article.created_username}}</td>
                    <td>{{article.title}}</td>
                    <td>{{article.created_date | friendlyDate}}</td>
                    <td>{{article.read_by}}</td>
                    <td>
                        <div class="btn-group" role="group">
                        <button
                                type="button"
                                class="btn btn-sm"
                                v-b-modal.Message-update-modal
                                @click="openMessage(article.id)">
                            Open
                        </button>
                        <!-- <button
                                type="button"
                                class="btn btn-danger btn-sm"
                                @click="onDeleteMessage(Message)">
                            View
                        </button> -->
                        </div>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
      </div>

    </div> <!-- container  -->
 </div> <!-- app -->
 

</template>

<script lang="ts">

import Vue from 'vue';
import Component from 'vue-class-component';
// import {  Prop } from 'vue-property-decorator';
import { friendlyDate } from '../filters/date-formatters';
import { seenByMe } from '../filters/text-formatters';
import AddMessage from '@/components/AddMessage.vue';
import ViewMessage from '@/components/ViewMessage.vue';
import MessageManager from '../store/message/message';
import AuthManager from '../store/auth/auth';
import { IMessage } from '../store/message/state';


@Component({
    name: 'MessagesComp',
    components: {
        AddMessage,
        ViewMessage,
    },
    filters: {
        friendlyDate,
        seenByMe,
    },
})
export default class MessagesComp extends Vue {
    private message: any;
    private showMessage: boolean =  false;
    private addNew: boolean = false;
    private currentLoggedInUser: string = '' ;

    // @Prop({type: Object as () => IMessage})
    // public messages!: IMessage[]; // notice the bang saying to compiler not to warn about no initial value

    public mounted() {
      this.currentLoggedInUser = AuthManager.getLoggedInUser();
      this.fetchMessages();
    }
    // private isReadByMe(message_reader: string) {
    //     return message_reader === this.currentLoggedInUser;
    // }

    // public isNewForMe(messageId: number) {
    //     console.log(messageId);
    //     const message = this.messages.find((m) => {
    //         return m.id === messageId;
    //     });
    //     if (message.read_by.includes(this.currentLoggedInUser)){
    //             return 'unseen';
    //     }

    //     return 'normal';

    // }

    get messages() {
        const ms = MessageManager.state.messages;
        // ms.forEach( (m) => {
        //     if (m.read_by.findIndex(this.isReadByMe) == -1) {
        //         m['read'] = 'unseen';
        //     }
        // });
        return ms;

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
<style lang="css" scoped>

.unseen {
    font-weight: bold;
}
.seen {
    font-weight: normal;
}
</style>
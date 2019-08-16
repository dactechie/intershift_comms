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
            <ViewMessage :message=message  :showMessage=showMessage v-if="showMessage"/>
            <table class="table table-hover">
                <thead>
                    <tr>
                    <th scope="col">Title</th>                    
                    <th scope="col">Created by</th>
                    <th scope="col">Create date</th>
                    <th scope="col">Read by</th>
                    <!-- <th scope="col">Read?</th> -->
                    <th></th>
                    </tr>
                </thead>
                <tbody>
                <tr v-for="article in messages" v-bind:key="article.id">        
                    <td>{{article.title}}</td>                    
                    <td>{{article.created_username}}</td>
                    <td>{{article.created_date}}</td>
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
import {  Prop } from 'vue-property-decorator';

import Vue from 'vue';
import Component from 'vue-class-component';

import AddMessage from '@/components/AddMessage.vue';
import ViewMessage from '@/components/ViewMessage.vue';
import MessageManager from '../store/message/message';
import { IMessage } from '../store/message/state';


@Component({
    name: 'MessagesComp',
    components: {
        AddMessage,
        ViewMessage,
    },
})
export default class MessagesComp extends Vue {
    private message: any;
    private showMessage: boolean =  false;
    private addNew: boolean = false;

    // @Prop({type: Object as () => IMessage})
    // public messages!: IMessage[]; // notice the bang saying to compiler not to warn about no initial value

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
                alert(this.message.content);
                this.showMessage = true;
            });
        });

    }
    private addedMessage() {
        // alert('cool');
        // this.showMessage = true;
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

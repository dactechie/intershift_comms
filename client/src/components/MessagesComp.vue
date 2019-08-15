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
            <AddMessage @savedMessage="messageSaved" v-if="addNew"/>
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
// import { Component, Prop } from 'vue-property-decorator';

import Vue from 'vue';
import Component from 'vue-class-component';
import axios from 'axios';

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

    private messages: any = null;
    private message: any;
    private showMessage: boolean =  false;
    private addNew: boolean = false;

    public mounted() {
      this.fetchMessages();
    }
    private openMessage(id: number) {
        MessageManager._getBMesgById(id)
        .then(mesg => {
            if (! mesg || !mesg.content) {
                MessageManager.dispatchGetMessage(id).then( res=>{
                    MessageManager._getBMesgById(id).then(r => {
                        this.message = r;                    
                        this.showMessage = true;
                    });                    
                });
            } else {
                this.message = mesg;
            }
        });        
    }
    private messageSaved() {
        alert('cool');
        //this.message = 'Succeuful';
        this.showMessage = true;
    }
    private toggleAddMessage() {
        this.addNew = !this.addNew;
    }
    private fetchMessages() {
        MessageManager.dispatchGetMessages().then(response => {
            console.log(response);
            this.messages = MessageManager.state.messages;
        });
    }


}

</script>

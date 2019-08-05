<template>
 <div id="app">
    <div class="container">
      <div class="row">
        <div class="col-sm-10">
            <h1>Messages</h1>
            <hr><br><br>
            <!-- <alert :message="message" v-if="showMessage"></alert> -->
            <!-- <button type="button" class="btn btn-success btn-sm" v-b-modal.Message-modal>Add Message</button> -->
            <button type="button" class="btn btn-success btn-sm" @click="toggleAddMessage">Add Message</button>
            <br><br>
            <AddMessage @savedMessage="messageSaved" v-if="addNew"/>
            <br><br>
            <table class="table table-hover">
                <thead>
                    <tr>
                    <th scope="col">Title</th>
                    <th scope="col">Content</th>
                    <th scope="col">Created by</th>
                    <th scope="col">Read by</th>
                    <!-- <th scope="col">Read?</th> -->
                    <th></th>
                    </tr>
                </thead>
                <tbody>
                <tr v-for="article in articles" v-bind:key="article.id">        
                    <td>{{article.title}}</td>
                    <td>{{article.content}}</td>
                    <td>{{article.created_user_id}}</td>
                    <td>{{article.read_by}}</td>
                    <td>
                        <div class="btn-group" role="group">
                        <button
                                type="button"
                                class="btn btn-warning btn-sm"
                                v-b-modal.Message-update-modal
                                @click="editMessage(Message)">
                            Edit
                        </button>
                        <button
                                type="button"
                                class="btn btn-danger btn-sm"
                                @click="onDeleteMessage(Message)">
                            View
                        </button>
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
// import { Component, Prop, Vue } from 'vue-property-decorator';

import Vue from 'vue';

import Component from 'vue-class-component';
import AddMessage from '@/components/AddMessage.vue';
import axios from 'axios';


@Component({
    name: 'MessagesComp',
    components: {
        AddMessage,
    },
})

export default class MessagesComp extends Vue {

    private articles: any = null;
    private message: string = '';
    private showMessage: boolean =  false;
    private addNew: boolean = false;

    public mounted() {
      this.fetchMessages();
    }
    private messageSaved() {
        alert('cool');
        this.message = 'Succeuful';
        this.showMessage = true;
    }
    private toggleAddMessage() {
        this.addNew = !this.addNew;
    }
    private fetchMessages() {
        axios.get('http://127.0.0.1:5000/messages').then((response) => {
          this.articles = response.data.messages;
        }, (error) => {
            alert(error);
        });
    }


}

</script>

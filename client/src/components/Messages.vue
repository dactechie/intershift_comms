<template>
 <div id="app">
    <div class="container">
        <div class="row">
        <div class="col-sm-10">
            <h1>Messages</h1>
            <hr><br><br>
            <alert :message=message v-if="showMessage"></alert>
            <button type="button" class="btn btn-success btn-sm" v-b-modal.Message-modal>Add Message</button>
            <br><br>
            <table class="table table-hover">
                <thead>
                    <tr>
                    <th scope="col">Title</th>
                    <th scope="col">Content</th>
                    <!-- <th scope="col">Read?</th> -->
                    <th></th>
                    </tr>
                </thead>
                <tbody>
                <tr v-for="article in articles" v-bind:key="article.id">        
                    <td>{{article.title}}</td>
                    <td>{{article.content}}</td>
                    <!-- <tr v-for="(Message, index) in Messages" :key="index">
                    <td>{{ Message.title }}</td>
                    <td>{{ Message.author }}</td> -->
                    <!-- <td>
                        <span v-if="Message.read">Yes</span>
                        <span v-else>No</span>
                    </td> -->
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
        <b-modal ref="addMessageModal"
            id="Message-modal"
            title="Add a new Message"
            hide-footer>
            <b-form @submit="onSubmit" @reset="onReset" class="w-100">
            <b-form-group id="form-title-group"
                            label="Title:"
                            label-for="form-title-input">
                <b-form-input id="form-title-input"
                                type="text"
                                v-model="addMessageForm.title"
                                required
                                placeholder="Enter title">
                </b-form-input>
                </b-form-group>
                <b-form-group id="form-content-group"
                            label="Content:"
                            label-for="form-content-input">
                    <b-form-input id="form-content-input"
                                type="text"
                                v-model="addMessageForm.content"
                                required
                                placeholder="Enter your message">
                    </b-form-input>
                </b-form-group>
                <!--<b-form-group id="form-read-group">
                <b-form-checkbox-group v-model="addMessageForm.read" id="form-checks">
                    <b-form-checkbox value="true">Read?</b-form-checkbox>
                </b-form-checkbox-group>
                </b-form-group> -->
                <b-button-group>
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
                </b-button-group>
            </b-form>
        </b-modal>
    </div>
 </div>
 

</template>

<script lang="ts">
// import { Component, Prop, Vue } from 'vue-property-decorator';
import Vue from 'vue';
import Component from 'vue-class-component';
import axios from 'axios';

// @Component({
//   props: {
//     propMessage: String
//   }
// })

interface NewMessage {
    title: string;
    content: string;
}

@Component
export default class Messages extends Vue {
    private articles: any = null;
    private message: string = '';
    private showMessage: boolean =  false;
    private addMessageForm: NewMessage = {
        title: '',
        content: '',
    };
    public mounted() {
      this.fetchMessages();
    }
    private fetchMessages() {
        axios.get('http://127.0.0.1:5000/messages').then((response) => {
          this.articles = response.data.messages;
        }, (error) => {
            alert(error);
        });
    }
    private addMessage(payload: NewMessage) {
      const path = 'http://localhost:5000/messages';
      axios.post(path, payload)
        .then(() => {
          this.fetchMessages();
          this.message = 'Message added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          alert('error ' + error);
          // console.log(error);
          this.fetchMessages();
        });
    }
    private initForm() {
      this.addMessageForm.title = '';
      this.addMessageForm.content = '';
      // this.addMessageForm.read = [];
    //   this.editForm.id = '';
    //   this.editForm.title = '';
    //   this.editForm.author = '';
    //   this.editForm.read = [];
    }
    private onSubmit(evt: any) {
      evt.preventDefault();
     // this.$refs.addMessageModal.hide();
      // let read = false;
      // if (this.addMessageForm.read[0]) read = true;
      const payload: NewMessage = {
        title: this.addMessageForm.title,
        content: this.addMessageForm.content,
      };
      this.addMessage(payload);
      this.initForm();
    }
    private onReset(evt: any) {
      evt.preventDefault();
      // this.$refs.addMessageModal.hide();
      this.initForm();
    }

}

</script>

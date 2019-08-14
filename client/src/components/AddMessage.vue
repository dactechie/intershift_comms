<template>
<!--
      <b-modal ref="addMessageModal"
            id="Message-modal"
            title="Add a new Message"
            hide-footer>
            -->
            <b-form @submit.prevent="onSubmit" @reset.prevent="onReset" class="w-100">
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
                    <textarea id="form-content-input"
                                rows="8"
                                v-model="addMessageForm.content"
                                required
                                placeholder="Enter your message (at least 10 characters)"
                                v-on:keydown.enter="$event.stopPropagation()">
                    </textarea>
                </b-form-group>


                <b-button-group>
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
                </b-button-group>
            </b-form>

        <!-- </b-modal> -->
       
</template>
                <!--<b-form-group id="form-read-group">
                <b-form-checkbox-group v-model="addMessageForm.read" id="form-checks">
                    <b-form-checkbox value="true">Read?</b-form-checkbox>
                </b-form-checkbox-group>
                </b-form-group> -->


<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import axios from 'axios';
import MessageManager from '../store/message/message';
import { IMessage } from '../store/message/state';
// import { Prop } from 'vue-property-decorator';

interface NewMessage {
    title: string;
    content: string;
}

@Component ({
  name: 'AddMessage',
})
export default class AddMessage extends Vue {
    private addMessageForm: NewMessage = {
        title: '',
        content: '',
    };

    private addMessage(payload: NewMessage) {
      const m: IMessage = {title : 'title',  content : 'content',   created_date : new Date()};
      m.title = payload.title;
      m.content = payload.content;
      m.created_date = new Date();
      MessageManager.dispatchDelayedAppend(m);
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
      // this.$refs.addMessageModal.hide();
      this.initForm();
    }
}
</script>
<style scoped>

textarea {
  width:100%;
}

</style>

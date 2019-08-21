<template>
<!--
      <b-modal ref="addMessageModal"
            id="Message-modal"
            title="Add a new Message"
            hide-footer>
            -->
            <v-form @submit.prevent="onSubmit" @reset.prevent="onReset" class="w-100">
      
                <v-text-field id="form-title-input"
                                type="text"
                                v-model="title"
                                required
                                placeholder="Enter title">
                </v-text-field>
             
        
                    <v-textarea id="form-content-input"
                                rows="8"
                                v-model="content"
                                required
                                placeholder="Enter your message (at least 10 characters)"
                                v-on:keydown.enter="$event.stopPropagation()">
                    </v-textarea>
              


            
                <v-btn type="submit" variant="primary">Submit</v-btn>
                <v-btn type="reset" variant="danger">Reset</v-btn>
            
            </v-form>

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

@Component ({
  name: 'AddMessage',
})
export default class AddMessage extends Vue {
    private title: string = '';
    private content: string = '';
    private message: IMessage = {
       title: '',
       content: '',
    };
    private initForm() {
      this.title = '';
      this.content = '';
    }

    private onSubmit(evt: any) {
      // this.$refs.addMessageModal.hide();
      this.message.title = this.title;
      this.message.content = this.content;
      MessageManager.dispatchDelayedAppend(this.message).then((res) => {
        this.$emit('added_message');
      }).catch((error) => {
         alert(error);
      });

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

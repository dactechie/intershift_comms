<template>

      <b-modal ref="viewMessageModal"
            id="Message-modal"
            title="View Message"
            v-show="true"
            hide-footer>
           
            <b-form class="w-100">
            <b-form-group id="form-title-group"
                            label="Title:"
                            label-for="form-title-input">
                <b-form-input id="form-title-input"
                                type="text"
                                readonly
                                v-model="message.title"
                                >
                </b-form-input>
                </b-form-group>
                <b-form-group id="form-content-group"
                            label="Content:"
                            label-for="form-content-input">
                    <textarea id="form-content-input"
                                rows="8"
                                v-model="message.content"
                                readonly                               
                                >
                    </textarea>
                </b-form-group>

            </b-form>

        </b-modal>
       
</template>



<script lang="ts">
import Vue from 'vue';
// import Component from 'vue-class-component';
import axios from 'axios';
import MessageManager from '../store/message/message';
import { IMessage } from '../store/message/state';
import { Component, Prop } from 'vue-property-decorator';


@Component ({
  name: 'ViewMessage',
})
export default class ViewMessage extends Vue {

    @Prop() private message!: IMessage;
    // @Prop(Boolean) private showMessage!: boolean;

    // $refs: {
    //   viewMessageModal: HTMLEl
    // }


    // public mount() {
    //   this.$refs['my-modal'].show();
    //   this.$refs.viewMessageModal.show();
    // }

    public beforeDestroy() {
        // this.showMessage = false;
    }
}
</script>
<style scoped>

textarea {
  width:100%;
}

</style>

<template>
   <v-app>
    <v-container style="max-width: 600px;">
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
            
    <MessagesTItems/>
     <!--
            <ViewMessage :message=message v-if="showMessage"/>-->
          </div>
      </div>

    </v-container> <!-- container  -->
 </v-app> <!-- app -->
 
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import MessagesTItems from '@/components/MessagesTItems.vue';
import AddMessage from '@/components/AddMessage.vue';
import ViewMessage from '@/components/ViewMessage.vue';
@Component({
  components: {
    MessagesTItems,
    AddMessage,
  },
})
export default class Home extends Vue {
    private addNew: boolean = false;
    private toggleAddMessage() {
        this.addNew = !this.addNew;
    }
    private addedMessage() {

    }

}
</script>

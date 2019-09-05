<template>
    <v-btn
      bottom
      color="pink"
      dark
      fab
      fixed
      right
      @click="dialog = !dialog"
    >
      <v-icon large color="darken-2">mdi-message-text</v-icon>

     <v-dialog
      v-model="dialog"
      width="800px"
    >
      <v-card>
        <v-card-title class="grey darken-2">
          Create a shift handover note.
        </v-card-title>
        <v-container>
          <v-row >
            <v-col cols="12" md="6">
              <v-text-field
                v-model="message.title"
                placeholder="Title"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
                <RichTextEditor v-model="message.content"  :value="message.content"/>
            </v-col>
          </v-row>
        </v-container>
        <v-card-actions>
        <v-checkbox 
            v-model="message.with_action"
            label="Check if it requires an action to be taken"
            ></v-checkbox>
            <!-- "`Requires Action ? ${message.with_action.toString()}`" -->
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="dialog = false"
          >Cancel</v-btn>
          <v-btn
            text
            @click="addMessage"
          >Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
        </v-btn>
</template>

<script>

import { mapActions } from 'vuex'
import RichTextEditor from '@/components/RichTextEditor'

export default {
    components:{
        RichTextEditor,
    },
    data: () => ({
      dialog: false,
      
      message: {
          title: '',
          content: '',
          with_action: false,
      },
    }),
    methods: {
        ...mapActions([
            'ADD_MESSAGE',
        ]),
        addMessage: function () {
            this.message.title = this.message.title.replace(/[^\w\s]/gi, '').trim()
            if (this.message.title.length <1) {
                alert("Must have a title")
                return;
            }
            this.message.content = this.message.content.trim()
            if (this.message.content.length < 5) {
                alert("The message must be more than 5 characters")
                return;
            }
            let _this = this
            this.ADD_MESSAGE(this.message).then(() => {
                // console.log("added message")
                this.$emit('addedMessage')
                _this.dialog = false
                
            })
        }
    },
}
</script>
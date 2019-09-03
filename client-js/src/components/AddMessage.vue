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
              <v-textarea
                v-model="message.content"
                auto-grow
                full-width
                outlined
                label="Notes"
                placeholder="Notes"
              ></v-textarea>
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
        <div>
                  <!--Use the component in the right place of the template--
                  <tiptap-vuetify
                    v-model="content"
                    :extensions="extensions"
                  />

                  <!- -Here's how to make a preview (optional)--
                  <h1>Preview</h1>
                  <hr>

                  <div
                    class="tiptap-vuetify-editor__content"
                    v-html="content"
                  />-->
                </div>
    </v-dialog>
        </v-btn>
</template>

<script>

import { mapActions } from 'vuex'
// import the component and the necessary extensions
// import { TiptapVuetify, Heading, Bold, Italic, Strike, Underline, Code, CodeBlock, Paragraph, BulletList, OrderedList,
//   ListItem, Link, Blockquote, HardBreak, HorizontalRule, History
// } from 'tiptap-vuetify'

export default {
    // components:{
    //   TiptapVuetify
    // },
    data: () => ({
      dialog: false,
      
      message: {
          title: '',
          content: '',
          with_action: false,
      },
       // declare extensions you want to use
    // extensions: [
    //   // you can specify options for extension
    //   new Heading({
    //     levels: [1, 2, 3]
    //   }),
    //   new Bold(),
    //   new Italic(),
    //   new Strike(),
    //   new Underline(),
    //   new Code(),
    //   new CodeBlock(),
    //   new Paragraph(),
    //   new BulletList(),
    //   new OrderedList(),
    //   new ListItem(),
    //   new Link(),
    //   new Blockquote(),
    //   new HardBreak(),
    //   new HorizontalRule(),
    //   new History()
    // ],
    // // starting content for the editor
    // content: `
    //   <h1>Yay Headlines!</h1>
    //   <p>All these <strong>cool tags</strong> are working now.</p>
    // `
    }),
    methods: {
        ...mapActions([
            'ADD_MESSAGE',
        ]),
        addMessage: function () {
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
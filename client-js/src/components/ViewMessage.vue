<template>

     <v-dialog
      v-model="dialog"
      width="1000px"
    >
      <v-card class="elevation-2">
        <v-card-title class="grey darken-2">
          View a shift handover note.
        </v-card-title>
        <v-container>
          <v-row >
            <v-col cols="12" md="6">
              <v-text-field
                v-model="message.title"
                :readonly="true"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
               <p v-html="content">
                    {{content}}
                </p>
            </v-col>
          </v-row>
        </v-container>
        <v-card-actions>
        <div v-if="message.actioned_by">
            Actioned by : {{message.actioned_by}}
        </div>
        <v-checkbox v-else-if="message.with_action && ! message.actioned_by"
            v-model="actioned"
            :label="`Mark Actioned ? ${actioned.toString()}`"
        ></v-checkbox>
        <v-checkbox v-else
            v-model="require_action_set_true"
            :label="`Requires Action ? ${require_action_set_true}`"
        ></v-checkbox>
        
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="closeMe"
          >Close</v-btn>

        </v-card-actions>
      </v-card>
    </v-dialog>

</template>

<script>

import {  mapGetters, mapActions } from 'vuex'

export default {
    data: () => ({
      dialog: true,
      content: '',
      actioned: false,
      require_action_set_true: false,
    }),
    props: ["message"],
    computed: mapGetters(['load_messages']),

    beforeMount () {       
        if (this.message.content) {
            this.content = this.message.content
            //this.action_required = this.message.requires_action
            return
        }
        this.LOAD_MESSAGE(this.message.id)
        .then(() => {
            let tmpMesg = this.load_messages.find(m =>
                m.id === this.message.id )
            this.content = tmpMesg.content
            if (tmpMesg['with_action']) {
                // console.log(' with action? ', tmpMesg['with_action'])
                this.with_action = true
            }
        })
    },
    beforeDestroy() {
        if (!this.message.with_action && this.require_action_set_true){
            this.message.with_action = true      
            this.UPDATE_MESSAGE(this.message).then((response) =>{
                console.log("update response", response)
            })
        } else if (this.actioned && !this.message.actioned_by) {
            this.message.actioned_by = 'me'
            this.UPDATE_MESSAGE(this.message).then((response) =>{
                console.log("update response", response)
            })
        }
    },
    methods: {
            ...mapActions([
            'LOAD_MESSAGE',
            'UPDATE_MESSAGE',
        ]),
        closeMe(){
            this.$emit('closeViewer', this.message)
            this.dialog = false
        },
    }
}
</script>
<template>
    <v-btn
      @click="dialog = !dialog"
    >
     <v-icon>view</v-icon>
    {{title}}

     <v-dialog
      v-model="dialog"
      width="800px"
    >
      <v-card>
        <v-card-title class="grey darken-2">
          View a shift handover note.
        </v-card-title>
        <v-container>
          <v-row >
            <v-col cols="12" md="6">
              <v-text-field
                v-model="viewingMessage.title"
                :readonly="true"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-textarea
                v-model="viewingMessage.content"
                :readonly="true"               
                full-width
                outlined
                label="Notes"
              ></v-textarea>
            </v-col>
          </v-row>
        </v-container>
        <v-card-actions>
          <!-- <v-btn
            text
            color="primary"
          >More</v-btn> -->
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="dialog = !dialog"
          >Close</v-btn>

        </v-card-actions>
      </v-card>
    </v-dialog>
    </v-btn>
</template>

<script>

import { mapActions, mapState } from 'vuex'

export default {
    data: () => ({
      dialog: false,
    }),
    
    props: ["message_id", "title"],

    computed: mapState([
            'viewingMessage'
    ]),
    mounted() {
        this.LOAD_MESSAGE(this.message_id)
    },
    methods: {
        ...mapActions([
            'LOAD_MESSAGE',
        ]),
        // closeMe(){
        //     this.$emit('closeViewer')
        // }
    }
}
</script>
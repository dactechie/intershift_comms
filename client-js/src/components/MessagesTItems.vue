<template>
<v-container >
    <v-timeline :dense="$vuetify.breakpoint.smAndDown">
        <v-layout row justify-center>
            <v-flex xs6>
                <v-slide-x-transition
                    group
                >
              <MessageTItem v-for="m in messages" :message="m" :key="m.id" />
                </v-slide-x-transition>
            </v-flex>
        </v-layout>
    </v-timeline>
</v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MessageTItem from './MessageTItem'


export default {
    components: {
        MessageTItem,
    },
    computed: {
        ...mapGetters([
            'load_messages',
        ]),
        messages () {
            return this.$store.getters.load_messages
        },
    },    
    mounted: function ()  {
         this.$nextTick(function () {
            // Code that will run only after the
            // entire view has been rendered
            this.LOAD_MESSAGES()
        })
    },
    methods: {
        ...mapActions([
            'LOAD_MESSAGES',
        ]),
    },
}

</script>
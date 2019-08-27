<template>
<v-container style="max-width: 600px;">
    <v-timeline :dense="$vuetify.breakpoint.smAndDown">
        
        <MessageTItem v-for="m in messages" :message="m" :key="m.id" />
        
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
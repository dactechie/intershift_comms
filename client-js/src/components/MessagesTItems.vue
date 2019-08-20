<template>
<v-container style="max-width: 600px;">
    <v-timeline :dense="$vuetify.breakpoint.smAndDown">
        
        <MessageTItem v-for="m in messages" :message="m" :key="m.id" />
        
    </v-timeline>
    
</v-container>
</template>

<script>
import { mapActions } from 'vuex'
import MessageTItem from './MessageTItem'

export default {
    components: {
        MessageTItem,
    },
    computed: {
        messages () {
            return this.$store.state.messages
        },
    },    
    mounted: function ()  {
         // this.$nextTick(function () {
            // Code that will run only after the
            // entire view has been rendered
            this.getMessages()
       // })
    },
    methods: {
        ...mapActions({
            getMessages: 'LOAD_MESSAGES',        
        }),
    },
    // data ()  {
    // //     return {
    // //     messages: [
    // //         {
    // //             id: 1,
    // //             author: "MJ",
    // //             title: " Title 1 !",
    // //             contentBrief: "Lorem ipsum dolor sit amet consec...",
    // //             datetime: "12/8/2019 (Yesterday at 5pm)",
    // //         },
    // //         {
    // //             id: 2,
    // //             author: "MD",
    // //             title: " Meg's Title !",
    // //             contentBrief: "Meg's messaage Lorem ipsum dolor sit amet consec...",
    // //             datetime: "13/8/2019 (Today at 3pm)",
    // //         }
    // //     ]
    // //   }
    // }
}

</script>
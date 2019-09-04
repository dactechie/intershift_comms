<template>

    <div class="caption">Read by:
        <v-chip :class="` ${item.color} white--text caption `" small v-for="(item, index) in read_by_list"  :key=index>
            <!-- <v-icon>{{icons[index]}}</v-icon> -->
            {{item.initials}}
        </v-chip>
    </div>
</template>

<script>
export default {
    name: 'ReadByUserBadges',
    props: ['read_by_list'],
    data: () => ({
        
        icons:  ['mdi-anchor', 'mdi-face'],
        
    }),
}
</script>

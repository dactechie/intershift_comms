<template>

    <div class="caption">Read by:
        <v-chip :class="` ${item} white--text caption `" small v-for="(item, index) in read_by_list"  :key=index>
            <!-- <v-icon>{{icons[index]}}</v-icon> -->
            {{item}}
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
<style lang="stylus" scoped>
.theme--light.v-chip.steve:not(.v-chip--active)  {
    background-color:tomato;

}
.theme--light.v-chip.aftab:not(.v-chip--active)  {
    background-color: lightblue ;

}
</style>
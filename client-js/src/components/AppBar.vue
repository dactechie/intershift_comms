<template>
        <v-app-bar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      app
      color="blue darken-3"
      dark
    >
      <v-toolbar-title
        style="width: 300px"
        class="ml-0 pl-4"
      >
        <span class="hidden-sm-and-down">Arcadia Handover notes</span>
      </v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        hide-details
        label="Search"
        class="hidden-sm-and-down"
      ></v-text-field>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-apps</v-icon>
      </v-btn>
        <v-btn icon to="/logout">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>
</template>
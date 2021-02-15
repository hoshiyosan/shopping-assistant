<template>
  <div>
    <v-app-bar color="deep-purple accent-4" dense dark>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title :title="subtitle">{{ title }}</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon v-for="(action, index) in navActions" :key="index" @click="action.callback">
        <v-icon>{{action.icon}}</v-icon>
      </v-btn>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    subtitle: String,
    navActions: Array
  },
};
</script>
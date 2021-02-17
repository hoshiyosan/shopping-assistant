<template>
  <div>
    <v-app-bar color="primary" dark dense fixed>
      <v-toolbar-title :title="subtitle">{{ title }}</v-toolbar-title>

      <v-spacer></v-spacer>

      <div class="actions" v-if="authenticated">
        <v-btn
          icon
          v-for="(action, index) in navActions"
          :key="index"
          @click="action.callback"
        >
          <v-icon>{{ action.icon }}</v-icon>
        </v-btn>
      </div>
    </v-app-bar>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState("auth", ["authenticated"]),
  },
  props: {
    title: String,
    subtitle: String,
    navActions: Array,
  },
};
</script>
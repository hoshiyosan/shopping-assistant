<template>
  <v-bottom-navigation color="primary" fixed hide-on-scroll grow>
    <v-btn
      :to="{ name: item.route }"
      v-for="item in navItems"
      :key="item.title"
      text
    >
      <span>{{ item.title }}</span>
      <v-icon>{{ item.icon }}</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
export default {
  props: {
    navItems: Array,
  },
};
</script>

<style>
.v-bottom-navigation--fixed {
  position: fixed !important;
}

.v-item-group.v-bottom-navigation .v-btn {
  height: inherit !important;
}
</style>
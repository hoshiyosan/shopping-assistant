<template>
  <v-navigation-drawer permanent expand-on-hover absolute>
    <v-list dense nav>
      <v-list-item
        v-for="item in navItems"
        :key="item.title"
        :to="{ name: item.route }"
        :title="item.title"
        link
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: {
    navItems: Array,
  },
};
</script>
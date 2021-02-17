<template>
  <v-list three-line v-if="shoppingLists">
    <template v-for="(shoppingList, index) in shoppingLists">
      <v-list-item :key="index">
        <v-list-item-avatar>
          <v-icon v-if="!shoppingList.thumbnail">mdi-clipboard-list</v-icon>
          <v-img
            v-if="shoppingList.thumbnail"
            :src="shoppingList.thumbnail"
          ></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-html="shoppingList.name"></v-list-item-title>
          <v-list-item-subtitle>
            {{ shoppingList.created | showDate }}
          </v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action>
          <slot name="actions" v-bind:shoppingList="shoppingList"></slot>
        </v-list-item-action>
      </v-list-item>
    </template>
  </v-list>
</template>

<script>
export default {
  props: {
    shoppingLists: Array,
  },
  methods: {
    onShoppingListSelected(shoppingList) {
      this.$emit("selected", shoppingList);
    },
  },
};
</script>
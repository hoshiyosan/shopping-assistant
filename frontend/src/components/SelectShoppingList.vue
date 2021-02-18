<template>
  <v-select
    :items="shoppingLists"
    item-text="name"
    label="Selectionnez une liste de courses"
    prepend-icon="mdi-clipboard-list"
    @change="onShoppingListChange"
    return-object
  ></v-select>
</template>

<script>
export default {
  data() {
    return { shoppingLists: [] };
  },
  props: {
    value: Object,
  },
  mounted() {
    this.$store
      .dispatch("shoppinglists/search", "")
      .then((shoppingLists) => (this.shoppingLists = shoppingLists));
  },
  methods: {
    onShoppingListChange(shoppingList) {
      this.$emit("input", shoppingList);
    },
  },
};
</script>
<template>
  <v-select
    :items="shoppingLists"
    item-text="name"
    label="Selectionnez des listes de courses"
    @change="onShoppingListChange"
    return-object
  ></v-select>
</template>

<script>
export default {
  data() {
    return { shoppingLists: [] };
  },
  mounted() {
    this.$store
      .dispatch("shoppinglists/search", "")
      .then((shoppingLists) => (this.shoppingLists = shoppingLists));
  },
  methods: {
    onShoppingListChange(shoppingList) {
      this.$emit("selected", shoppingList);
    },
  },
};
</script>
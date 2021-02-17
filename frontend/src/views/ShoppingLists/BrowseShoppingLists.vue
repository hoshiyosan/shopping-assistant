<template>
  <main style="position: relative">
    <h2><v-icon>mdi-clipboard-list</v-icon> Listes de courses</h2>

    <div class="actions" style="position: absolute; right: 0; top: 8px">
      <v-btn fab color="primary" dark small @click="createShoppingList()">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </div>

    <v-text-field
      v-model="search"
      label="Chercher une liste"
      append-icon="mdi-magnify"
      @input="queryShoppingLists()"
    />
    <shoppinglists-list :shopping-lists="shoppingLists">
      <template v-slot:actions="slot">
        <div>
          <v-btn icon @click="editShoppingList(slot.shoppingList._id)">
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon>mdi-cart-arrow-right</v-icon>
          </v-btn>
        </div>
      </template>
    </shoppinglists-list>
  </main>
</template>

<script>
// TODO: remove

import ShoppinglistsList from "@/components/ShoppinglistsList";

export default {
  components: { ShoppinglistsList },
  data() {
    return { search: "", shoppingLists: [] };
  },
  mounted() {
    this.queryShoppingLists();
  },
  methods: {
    queryShoppingLists() {
      this.$store
        .dispatch("shoppinglists/search", this.search)
        .then((shoppingLists) => (this.shoppingLists = shoppingLists));
    },
    editShoppingList(shoppingListUID) {
      this.$router.push({
        name: "EditShoppingList",
        params: { shoppingListUID },
      });
    },
    createShoppingList() {
      this.$store.dispatch("shoppinglists/createEmpty").then((shoppingList) => {
        this.$router.push({
          name: "EditShoppingList",
          params: { shoppingListUID: shoppingList._id },
        });
      });
    },
  },
};
</script>
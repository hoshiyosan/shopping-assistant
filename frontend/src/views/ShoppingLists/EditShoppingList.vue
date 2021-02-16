<template>
  <main>
    <v-text-field label="Titre de la liste" v-model="shoppingList.name" />
    <v-tabs
      v-model="currentTab"
      fixed-tabs
      background-color="secondary"
      center-active
      dark
    >
      <v-tab href="#recipes">Recettes</v-tab>
      <v-tab href="#ingredients">Ingrédients</v-tab>
      <v-tab href="#partager">Partager</v-tab>
    </v-tabs>

    <v-tabs-items v-model="currentTab">
      <v-tab-item value="recipes">
        <v-container> rec</v-container>
      </v-tab-item>
      <v-tab-item value="ingredients">
        <v-container>
          <edit-ingredients v-model="shoppingList.ingredients" />
        </v-container>
      </v-tab-item>
      <v-tab-item value="partager">
        <v-container>par</v-container>
      </v-tab-item>
    </v-tabs-items>
  </main>
</template>

<script>
import EditIngredients from "@/components/EditIngredients";

export default {
  components: { EditIngredients },
  data() {
    return { currentTab: "recipes", shoppingList: null };
  },
  mounted() {
    const shoppingListUID = this.$route.params.shoppingListUID;
    this.$store
      .dispatch("shoppinglists/get", shoppingListUID)
      .then((shoppingList) => (this.shoppingList = shoppingList));
  },
};
</script>
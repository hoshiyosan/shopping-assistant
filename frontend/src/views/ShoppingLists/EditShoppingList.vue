<template>
  <main v-if="shoppingList">
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
        <v-container>
          <recipes-list :recipes="shoppingList.recipes">
            <template v-slot:actions="slot">
              <div style="display: flex">
                <v-text-field
                  append-icon="mdi-account"
                  type="number"
                  v-model="slot.recipe.diners"
                  style="width: 4em; margin-right: 20px !important"
                />
                <v-btn icon color="red" @click="removeRecipe(slot.recipe)">
                  <v-icon>mdi-delete</v-icon>
                </v-btn>
              </div>
            </template>
          </recipes-list>
        </v-container>
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

    <v-btn color="primary" @click="saveShoppingList()">
      <v-icon>mdi-content-save</v-icon> Enregistrer
    </v-btn>
    <v-btn color="red" dark @click="deleteShoppingList()">
      <v-icon>mdi-delete</v-icon> Supprimer
    </v-btn>
  </main>
</template>

<script>
import EditIngredients from "@/components/EditIngredients";
import RecipesList from "@/components/RecipesList";

export default {
  components: { EditIngredients, RecipesList },
  data() {
    return { currentTab: "recipes", shoppingList: null };
  },
  mounted() {
    const shoppingListUID = this.$route.params.shoppingListUID;
    this.$store
      .dispatch("shoppinglists/get", shoppingListUID)
      .then((shoppingList) => (this.shoppingList = shoppingList));
  },
  methods: {
    saveShoppingList() {
      this.$store
        .dispatch("shoppinglists/update", this.shoppingList)
        .then(() => this.$router.push({ name: "BrowseShoppingLists" }));
    },
    removeRecipe(removedRecipe) {
      this.shoppingList.recipes = this.shoppingList.recipes.filter(
        (recipe) => recipe.uid != removedRecipe.uid
      );
    },
    deleteShoppingList() {
      this.$store
        .dispatch("shoppinglists/delete", this.shoppingList._id)
        .then(() => this.$router.push({ name: "BrowseShoppingLists" }));
    },
  },
};
</script>
<template>
  <v-container style="position: relative">
    <h2><v-icon>mdi-noodles</v-icon> Recettes</h2>

    <div class="actions" style="position: absolute; right: 0; top: 8px">
      <v-btn fab color="primary" dark small @click="createRecipe()">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </div>

    <v-text-field
      v-model="search"
      label="Chercher une recette"
      append-icon="mdi-magnify"
      @input="queryRecipes()"
    />
    <recipes-list :recipes="recipes">
      <template v-slot:actions="slot">
        <div>
          <v-btn icon @click="editRecipe(slot.recipe._id)">
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
          <v-btn icon @click="startAddingToShoppingList(slot.recipe)">
            <v-icon>mdi-clipboard-list</v-icon>
          </v-btn>
        </div>
      </template>
    </recipes-list>

    <!--
    <v-dialog v-model="isAddingRecipe" width="500">
      <v-card>
        <v-card-title class="headline grey lighten-2">
          Ajouter aux listes
        </v-card-title>

        <v-card-text>
          <select-shopping-list @selected="onShoppingListSelected" />
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="cancelAddToShoppingList()">
            Annuler
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    -->
    <add-shoppinglist-recipe-dialog
      v-model="isAddingRecipe"
      :recipe="selectedRecipe"
    />
  </v-container>
</template>


<script>
import RecipesList from "@/components/RecipesList";
//import SelectShoppingList from "@/components/SelectShoppingList";
import AddShoppinglistRecipeDialog from "@/components/AddShoppinglistRecipeDialog";

export default {
  components: { RecipesList, AddShoppinglistRecipeDialog },
  data() {
    return {
      search: "",
      recipes: null,
      isAddingRecipe: false,
      selectedRecipe: null,
    };
  },
  mounted() {
    this.queryRecipes();
  },
  methods: {
    /**
     * Retrieve a fresh last of recipes based on search query.
     */
    queryRecipes() {
      this.$store
        .dispatch("recipes/search", this.search)
        .then((recipes) => (this.recipes = recipes));
    },
    editRecipe(recipeUID) {
      this.$router.push({ name: "EditRecipe", params: { recipeUID } });
    },
    createRecipe() {
      this.$store.dispatch("recipes/createEmpty").then((recipe) => {
        this.$router.push({
          name: "EditRecipe",
          params: { recipeUID: recipe._id },
        });
      });
    },
    startAddingToShoppingList(recipe) {
      this.selectedRecipe = recipe;
      this.isAddingRecipe = true;
    },
  },
};
</script>
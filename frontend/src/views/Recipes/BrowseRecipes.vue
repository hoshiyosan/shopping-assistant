<template>
  <v-container>
    <h2>Recettes</h2>
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
          <v-btn icon>
            <v-icon>mdi-basket-plus</v-icon>
          </v-btn>
        </div>
      </template>
    </recipes-list>
  </v-container>
</template>


<script>
import RecipesList from "@/components/RecipesList";

export default {
  components: { RecipesList },
  data() {
    return { search: "", recipes: null };
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
  },
};
</script>
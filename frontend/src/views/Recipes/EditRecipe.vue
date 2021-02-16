<template>
  <main v-if="recipe">
    <v-tabs
      fixed-tabs
      background-color="secondary"
      center-active
      dark
      v-model="currentTab"
    >
      <v-tab href="#informations" key="recipe-info">Recette</v-tab>
      <v-tab href="#ingredients">Ingrédients</v-tab>
      <v-tab href="#partager">Partager</v-tab>
    </v-tabs>

    <v-tabs-items v-model="currentTab">
      <!-- tabs edit recipe information / steps -->

      <v-tab-item value="informations">
        <v-container>
          <div style="display: flex">
            <v-avatar size="150">
              <v-icon large>mdi-noodles</v-icon>
            </v-avatar>

            <div style="flex: 1">
              <v-text-field
                v-model="recipe.name"
                label="Nom de la recette"
                prepend-icon="mdi-noodles"
              />
              <v-text-field
                v-model="recipe.diners"
                label="Nombre de personnes"
                prepend-icon="mdi-account"
                type="number"
              />
            </div>
          </div>

          <h3>Etapes de la recette</h3>
          <edit-recipe-steps v-model="recipe.steps" />
        </v-container>
      </v-tab-item>
      <v-tab-item value="ingredients">
        <v-container>
          <edit-ingredients v-model="recipe.ingredients"></edit-ingredients>
        </v-container>
      </v-tab-item>
      <v-tab-item value="partager">Partager</v-tab-item>
    </v-tabs-items>

    <v-btn color="primary" @click="saveRecipe()">
      <v-icon>mdi-content-save</v-icon> Enregistrer
    </v-btn>
  </main>
</template>

<script>
import EditRecipeSteps from "@/components/EditRecipeSteps";
import EditIngredients from "@/components/EditIngredients";

export default {
  components: { EditRecipeSteps, EditIngredients },
  data() {
    return {
      currentTab: "recipe-info",
      recipe: null,
      ingredientQuantity: { ingredient: "brocoli", quantity: 250, unit: "g" },
    };
  },
  mounted() {
    const recipeUID = this.$route.params.recipeUID;
    this.$store
      .dispatch("recipes/get", recipeUID)
      .then((recipe) => (this.recipe = recipe));
  },
  methods: {
    saveRecipe() {
      this.$store
        .dispatch("recipes/update", this.recipe)
        .then(() => this.$router.push({ name: "BrowseRecipes" }));
    },
  },
};
</script>
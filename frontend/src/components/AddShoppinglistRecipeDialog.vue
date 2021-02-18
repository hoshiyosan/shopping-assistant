<template>
  <v-dialog v-model="showDialog" width="500">
    <v-card>
      <v-card-title class="headline grey lighten-2">
        Ajouter une recette à la liste
      </v-card-title>

      <v-card-text>
        <v-text-field
          v-if="recipe"
          :value="recipe.name"
          prepend-icon="mdi-noodles"
          readonly
        />
        <select-shopping-list v-model="shoppingList" />
        <v-text-field
          v-model="diners"
          v-if="shoppingList"
          prepend-icon="mdi-account"
          label="Nombre de convives"
          type="number"
        />
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="red" text @click="closeDialog()"> Annuler </v-btn>
        <v-btn
          color="primary"
          text
          v-if="shoppingList && diners"
          @click="addRecipeToShoppingList()"
        >
          Ajouter
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import SelectShoppingList from "./SelectShoppingList";

export default {
  components: { SelectShoppingList },
  data() {
    return { showDialog: false, shoppingList: null, diners: null };
  },
  props: {
    value: Boolean,
    recipe: Object,
  },
  watch: {
    value(showDialog) {
      this.showDialog = showDialog;
    },
  },
  methods: {
    addRecipeToShoppingList() {
      this.$store.dispatch("shoppinglists/addRecipe", {
        shoppingListUID: this.shoppingList._id,
        recipeData: {
          uid: this.recipe._id,
          name: this.recipe.name,
          diners: this.diners,
          thumbnail: this.recipe.thumbnail,
        },
      });
      this.closeDialog();
    },

    closeDialog() {
      this.$emit("input", false);
    },
  },
};
</script>
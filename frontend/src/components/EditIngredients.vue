<template>
  <div>
    <edit-ingredient-quantity
      v-for="(_, index) in ingredients"
      :key="index"
      v-model="ingredients[index]"
    />
    <v-btn color="secondary" @click="addEmptyIngredient()">
      <v-icon>mdi-plus</v-icon> Ajouter un ingrédient
    </v-btn>

    <v-btn color="secondary" @click="showCreateIngredientDialog = true">
      <v-icon>mdi-plus</v-icon> Créer un ingrédient
    </v-btn>

    <create-ingredient-dialog
      v-model="showCreateIngredientDialog"
      @created="addIngredient"
    />
  </div>
</template>

<script>
import EditIngredientQuantity from "./EditIngredientQuantity";
import CreateIngredientDialog from "./CreateIngredientDialog";

export default {
  components: { EditIngredientQuantity, CreateIngredientDialog },
  data() {
    return { ingredients: [], showCreateIngredientDialog: false };
  },
  props: {
    value: Array,
  },
  watch: {
    value: {
      immediate: true,
      handler(changedIngredients) {
        this.ingredients = changedIngredients;
      },
    },
  },
  methods: {
    addIngredient(ingredient) {
      console.log("add ingredient", ingredient);
      this.ingredients.push({
        ingredient_uid: ingredient._id,
        quantity: null,
        unit: ingredient.unit,
      });
      this.$emit("input", this.ingredients);
    },
    addEmptyIngredient() {
      this.ingredients.push({ ingredient: null, quantity: null, unit: null });
      this.$emit("input", this.ingredients);
    },
  },
};
</script>
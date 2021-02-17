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

    show: {{ showCreateIngredientDialog }}

    <create-ingredient-form v-model="showCreateIngredientDialog" />
  </div>
</template>

<script>
import EditIngredientQuantity from "./EditIngredientQuantity";
import CreateIngredientForm from "./CreateIngredientForm";

export default {
  components: { EditIngredientQuantity, CreateIngredientForm },
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
    addEmptyIngredient() {
      this.ingredients.push({ ingredient: null, quantity: null, unit: null });
    },
  },
};
</script>
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
    {{ ingredients }}
  </div>
</template>

<script>
import EditIngredientQuantity from "./EditIngredientQuantity";

export default {
  components: { EditIngredientQuantity },
  data() {
    return { ingredients: [] };
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
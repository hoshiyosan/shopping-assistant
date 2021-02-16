<template>
  <main style="display: flex">
    <v-autocomplete
      :value="ingredientQuantity.ingredient_uid"
      :items="matchingIngredients"
      item-text="name"
      item-value="_id"
      return-object
      label="ingrédient"
      @change="onIngredientChange"
      style="flex: 2"
    ></v-autocomplete>
    <v-text-field
      label="quantité"
      type="number"
      :value="ingredientQuantity.quantity"
      @input="onQuantityChange"
      style="flex: 1"
    />
    <v-select
      label="unité"
      :value="ingredientQuantity.unit"
      :items="units"
      item-text="name"
      item-value="value"
      @change="onUnitChange"
      style="flex: 1"
    />
  </main>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      searchIngredient: "",
      ingredientQuantity: null,
      matchingIngredients: [],
    };
  },
  computed: {
    ...mapState("ingredients", ["units"]),
  },
  props: {
    value: Object,
  },
  watch: {
    value: {
      immediate: true,
      handler(changedIngredientQuantity) {
        this.ingredientQuantity = changedIngredientQuantity;
      },
    },
  },
  mounted() {
    this.queryIngredients();
  },
  methods: {
    queryIngredients() {
      this.$store
        .dispatch("ingredients/search", this.searchIngredient)
        .then((ingredients) => (this.matchingIngredients = ingredients));
    },
    updateProperties(properties) {
      const ingredientQuantity = Object.assign({}, this.ingredientQuantity);
      for (let property of Object.keys(properties)) {
        ingredientQuantity[property] = properties[property];
      }
      this.$emit("input", ingredientQuantity);
    },
    onIngredientChange(newIngredient) {
      this.updateProperties({
        ingredient_uid: newIngredient._id,
        unit: newIngredient.unit,
      });
    },
    onQuantityChange(newQuantity) {
      let quantity = parseFloat(newQuantity);
      quantity = isNaN(quantity) ? null : quantity;
      this.updateProperties({ quantity });
    },
    onUnitChange(newUnit) {
      this.updateProperties({ unit: newUnit });
    },
  },
};
</script>
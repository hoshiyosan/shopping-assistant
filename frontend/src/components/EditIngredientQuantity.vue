<template>
  <div v-if="ingredientQuantity" style="display: flex">
    <autocomplete-ingredient v-model="ingredientQuantity.ingredient" />
    <v-text-field
      v-model="ingredientQuantity.quantity"
      label="quantité"
      type="number"
      @input="notifyObservers()"
    />
    <v-select
      label="unité"
      item-text="name"
      item-value="value"
      v-model="ingredientQuantity.unit"
      @change="notifyObservers()"
      :items="units"
    />
    {{ ingredientQuantity }}
  </div>
</template>

<script>
import { mapState } from "vuex";
import AutocompleteIngredient from "./AutocompleteIngredient";

export default {
  components: { AutocompleteIngredient },
  data() {
    return { ingredientQuantity: null };
  },
  computed: {
    normalizedIngredientQuantity() {
      const normalized = Object.assign({}, this.ingredientQuantity);
      try {
        normalized.quantity = parseFloat(this.ingredientQuantity.quantity);
      } catch {
        normalized.quantity = null;
      }
      return normalized;
    },
    ...mapState("ingredients", ["units"]),
  },
  props: {
    value: Object,
  },
  watch: {
    value: {
      immediate: true,
      handler(changedIngredientQuantity) {
        console.log("ingredient quantity changed", changedIngredientQuantity);
        this.ingredientQuantity = changedIngredientQuantity;
      },
    },
  },
  methods: {
    notifyObservers() {
      this.$emit("input", this.normalizedIngredientQuantity);
    },
  },
};
</script>
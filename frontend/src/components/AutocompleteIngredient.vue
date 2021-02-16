<template>
  <main>
    <v-autocomplete
      v-model="selectedIngredient"
      :items="matchingIngredients"
      item-text="name"
      item-value="_id"
      :search-input.sync="search"
      @change="notifyObservers()"
    />
  </main>
</template>

<script>
export default {
  data() {
    return { search: "", matchingIngredients: [], selectedIngredient: null };
  },
  props: {
    value: String,
  },
  watch: {
    search(query) {
      console.log("search changed");
      this.$store
        .dispatch("ingredients/search", query)
        .then((ingredients) => (this.matchingIngredients = ingredients));
    },
  },
  methods: {
    notifyObservers() {
      this.$emit("input", this.selectedIngredient);
    },
  },
};
</script>
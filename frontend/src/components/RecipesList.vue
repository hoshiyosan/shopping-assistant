<template>
  <v-list three-line v-if="recipes">
    <template v-for="(recipe, index) in recipes">
      <v-list-item :key="index">
        <v-list-item-avatar>
          <v-icon v-if="!recipe.thumbnail">mdi-noodles</v-icon>
          <v-img v-if="recipe.thumbnail" :src="recipe.thumbnail"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-html="recipe.name"></v-list-item-title>
          <v-list-item-subtitle>
            {{ recipe.diners }} personne(s)
          </v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action>
          <slot name="actions" v-bind:recipe="recipe"></slot>
        </v-list-item-action>
      </v-list-item>
    </template>
  </v-list>
</template>

<script>
export default {
  props: {
    recipes: Array,
  },
  methods: {
    onRecipeSelected(recipe) {
      this.$emit("selected", recipe);
    },
  },
};
</script>
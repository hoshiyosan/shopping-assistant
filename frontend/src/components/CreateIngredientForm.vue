<template>
  <v-dialog with="500" v-model="showDialog">
    <v-card>
      <v-card-title class="headline grey lighten-2">
        Créer un ingrédient
      </v-card-title>

      <v-card-text>
        <form @submit.prevent="onSubmit()">
          <v-text-field
            label="Nom de l'ingrédient"
            v-model="ingredient.name"
            required
          />
          <v-select
            label="Unité par défaut"
            v-model="ingredient.unit"
            :items="units"
            item-text="name"
            item-value="value"
          />
          <v-select
            label="Catégorie d'ingrédient"
            v-model="ingredient.category"
            :items="categories"
            item-text="name"
            item-value="value"
            required
          />
          {{ ingredient }}

          <v-btn type="submit" color="primary">Créer un ingrédient</v-btn>
        </form>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="red" text @click="cancelAddToShoppingList()">
          Annuler
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      showDialog: false,
      ingredient: { name: "", unit: null, category: null },
    };
  },
  props: {
    value: Boolean,
  },
  computed: {
    ...mapState("ingredients", ["units", "categories"]),
  },
  watch: {
    value(showDialog) {
      this.showDialog = showDialog;
    },
  },
  methods: {
    onSubmit() {
      const newIngredient = Object.assign({}, this.ingredient);
      this.$store
        .dispatch("ingredients/create", newIngredient)
        .then(
          (createdIngredient) => this.$emit("created", createdIngredient),
          this.closeDialog()
        );
    },
    closeDialog() {
      this.$emit("input", false);
    },
  },
};
</script>
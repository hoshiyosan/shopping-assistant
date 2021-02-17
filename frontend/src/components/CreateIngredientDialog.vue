<template>
  <v-dialog with="500" v-model="showDialog" @click:outside="closeDialog()">
    <form @submit.prevent="onSubmit()">
      <v-card>
        <v-card-title class="headline grey lighten-2">
          Créer un ingrédient
        </v-card-title>

        <v-card-text>
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
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="closeDialog()"> Annuler </v-btn>
          <v-btn color="primary" type="submit" text> Créer </v-btn>
        </v-card-actions>
      </v-card>
    </form>
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
        .then((createdIngredient) => {
          this.$emit("created", createdIngredient);
          this.closeDialog();
        });
    },
    closeDialog() {
      console.log("close dialog");
      this.$emit("input", false);
    },
  },
};
</script>
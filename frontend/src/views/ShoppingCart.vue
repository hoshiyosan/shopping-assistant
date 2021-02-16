<template>
  <main>
    <header style="position: relative; margin-bottom: 15px">
      <h2><v-icon>mdi-cart</v-icon> Caddy</h2>

      <v-btn
        style="position: absolute; top: 0; right: 0"
        color="primary"
        v-if="totalRemaining === 0"
      >
        Terminer
      </v-btn>
    </header>

    <v-expansion-panels>
      <v-expansion-panel
        v-for="category in ingredientsByCategories"
        :key="category.name"
      >
        <v-expansion-panel-header>
          <strong :class="{ done: category.done }">
            {{ category.name }} ({{ category.remaining }})
          </strong>
        </v-expansion-panel-header>

        <v-expansion-panel-content>
          <v-list dense>
            <v-list-item-group color="primary">
              <v-list-item
                v-for="(ingredient, index) in category.ingredients"
                :key="index"
              >
                <v-list-item-content>
                  <v-list-item-title
                    v-text="ingredient.name"
                  ></v-list-item-title>
                  <v-list-item-subtitle>
                    {{ ingredient.quantity }}
                    {{ ingredient.unit }}
                  </v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-action>
                  <v-checkbox v-model="ingredient.done" />
                </v-list-item-action>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </main>
</template>

<script>
const CART_INGREDIENTS = [
  {
    name: "Poulet",
    quantity: 250,
    unit: "grammes",
    category: "Viandes",
    done: false,
  },
  {
    name: "Jambon",
    quantity: 4,
    unit: "tranches",
    category: "Viandes",
    done: false,
  },
  {
    name: "Poivron",
    quantity: 2,
    unit: null,
    category: "Fruits et Légumes",
    done: false,
  },
  {
    name: "Oignons",
    quantity: 3,
    unit: null,
    category: "Fruits et Légumes",
    done: false,
  },
  {
    name: "Crème fraîche",
    quantity: 50,
    unit: "millilitres",
    category: "Laitages",
    done: false,
  },
  {
    name: "Lait",
    quantity: 5,
    unit: "litres",
    category: "Laitages",
    done: false,
  },
];

export default {
  data() {
    return {
      cartIngredients: CART_INGREDIENTS,
    };
  },
  computed: {
    totalRemaining() {
      let count = 0;
      for (let ingredient of this.cartIngredients) {
        if (!ingredient.done) {
          count++;
        }
      }
      return count;
    },
    ingredientsByCategories() {
      const categories = {};
      for (let ingredient of this.cartIngredients) {
        if (categories[ingredient.category] == undefined) {
          categories[ingredient.category] = {
            name: ingredient.category,
            done: true,
            remaining: 0,
            ingredients: [],
          };
        }
        if (!ingredient.done) {
          categories[ingredient.category].done = false;
          categories[ingredient.category].remaining++;
        }
        categories[ingredient.category].ingredients.push(ingredient);
      }
      return Object.values(categories);
    },
  },
};
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
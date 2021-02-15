<template>
  <v-app>
    <main-navigation :title="app.title" :subtitle="app.subtitle" />

    <v-sheet style="position: relative; height: 100%">
      <v-container>
        <router-view />
      </v-container>

      <side-navigation
        :title="title"
        :subtitle="subtitle"
        :nav-items="navItems"
        v-if="!$vuetify.breakpoint.mobile"
      />
    </v-sheet>

    <bottom-navigation
      :title="title"
      :subtitle="subtitle"
      :nav-items="navItems"
      v-if="$vuetify.breakpoint.mobile"
    />
  </v-app>
</template>

<script>
import MainNavigation from "@/views/Navigation/MainNavigation";
import SideNavigation from "@/views/Navigation/SideNavigation";
import BottomNavigation from "@/views/Navigation/BottomNavigation";

export default {
  components: { MainNavigation, SideNavigation, BottomNavigation },
  data() {
    return {
      app: {
        title: "Shopping Assistant",
        subtitle: "Manage your ingredients!",
      },
      navItems: [
        {
          title: "Recettes",
          route: "Recipes",
          icon: "mdi-noodles",
        },
        {
          title: "Mes listes",
          route: "ShoppingLists",
          icon: "mdi-clipboard-list",
        },
        {
          title: "Mon caddy",
          route: "ShoppingCart",
          icon: "mdi-cart",
        },
        {
          title: "Mon frigo",
          route: "Fridge",
          icon: "mdi-fridge",
        },
      ],
    };
  },
};
</script>
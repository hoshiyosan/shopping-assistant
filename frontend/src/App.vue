<template>
  <v-app>
    <main-navigation
      v-if="authenticated"
      :title="app.title"
      :subtitle="app.subtitle"
      :nav-actions="navActions"
    />

    <v-sheet style="position: relative; height: 100%">
      <v-container>
        <router-view />
      </v-container>

      <side-navigation
        :nav-items="navItems"
        v-if="authenticated && !$vuetify.breakpoint.mobile"
      />
    </v-sheet>

    <bottom-navigation
      :nav-items="navItems"
      v-if="authenticated && $vuetify.breakpoint.mobile"
    />
  </v-app>
</template>

<script>
import { mapState } from "vuex";
import MainNavigation from "@/views/Navigation/MainNavigation";
import SideNavigation from "@/views/Navigation/SideNavigation";
import BottomNavigation from "@/views/Navigation/BottomNavigation";

export default {
  components: { MainNavigation, SideNavigation, BottomNavigation },
  computed: {
    ...mapState("auth", ["authenticated"]),
  },
  data() {
    return {
      app: {
        title: "Shopping Assistant",
        subtitle: "Manage your ingredients!",
      },
      navItems: [
        {
          title: "Recettes",
          route: "BrowseRecipes",
          icon: "mdi-noodles",
        },
        {
          title: "Mes listes",
          route: "BrowseShoppingLists",
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
      navActions: [
        {
          icon: "mdi-account-circle",
          callback: () => {
            // [EditAccountInfo] redirect to EditAccountInfo page
            if (this.$route.name !== "EditAccountInfo")
              this.$router.push({ name: "EditAccountInfo" });
          },
        },
        {
          icon: "mdi-power",
          callback: () => {
            // [logout] remove credentials and redirect to login if necessary
            this.$store.dispatch("auth/logout").then(() => {
              if (this.$route.name !== "Login")
                this.$router.push({ name: "Login" });
            });
          },
        },
      ],
    };
  },
};
</script>
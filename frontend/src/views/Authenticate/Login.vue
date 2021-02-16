<template>
  <v-card class="mx-auto my-12" max-width="374">
    <v-card-text>
      <form @submit.prevent="sendLogin()">
        <h2>Login</h2>
        <v-text-field label="Email" v-model="credentials.email" required />
        <v-text-field
          label="Password"
          type="password"
          v-model="credentials.password"
          required
        />
        <v-btn color="primary" type="submit">Connexion</v-btn>
      </form>

      <div style="margin-top: 1em">
        or
        <router-link :to="{ name: 'Register' }">
          create an account
        </router-link>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data() {
    return { credentials: { email: null, password: null } };
  },
  methods: {
    sendLogin() {
      this.$store
        .dispatch("auth/login", this.credentials)
        .then(() => this.$router.push({ name: "Welcome" }));
    },
  },
};
</script>
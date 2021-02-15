<template>
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
</template>

<script>
export default {
  data() {
    return { credentials: { email: null, password: null } };
  },
  methods: {
    sendLogin() {
      this.$store.dispatch("auth/login", this.credentials);
    },
  },
};
</script>
<template>
  <v-card class="mx-auto my-12" max-width="374">
    <v-card-text>
      <form @submit.prevent="registerAccount()">
        <h2>Register</h2>
        <v-text-field label="Prénom" v-model="account.first_name" required />
        <v-text-field label="Nom" v-model="account.last_name" required />
        <v-text-field label="Email" v-model="account.email" required />
        <v-text-field
          label="Password"
          type="password"
          v-model="account.password"
          required
        />
        <v-btn color="primary" type="submit">Inscription</v-btn>
      </form>

      <div style="margin-top: 1em">
        or
        <router-link :to="{ name: 'Register' }">
          login with an existing account
        </router-link>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  data() {
    return { account: { email: null, password: null } };
  },
  methods: {
    registerAccount() {
      this.$store.dispatch("accounts/create", this.account).then(() => {
        this.$store
          .dispatch("auth/login", {
            email: this.account.email,
            password: this.account.password,
          })
          .then(() => this.$router.push({ name: "Welcome" }));
      });
    },
  },
};
</script>
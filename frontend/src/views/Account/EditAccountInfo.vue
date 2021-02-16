<template>
  <main>
    <h2>Mon compte</h2>
    {{ currentAccount }}
  </main>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState("accounts", ["currentAccount"]),
  },
};
</script>
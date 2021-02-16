<template>
  <div>
    <div
      v-for="(step, index) in steps"
      :key="index"
      style="display: flex; align-items: center"
    >
      <v-btn icon color="red" @click="deleteStepByIndex(index)"
        ><v-icon>mdi-delete</v-icon></v-btn
      >
      <v-text-field
        :label="'Etape ' + index"
        v-model="steps[index]"
        @input="notifyObservers()"
      />
    </div>

    <v-btn color="secondary" @click="addEmptyStep()">
      <v-icon>mdi-plus</v-icon> Ajouter une étape
    </v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return { steps: [] };
  },
  props: {
    value: Array,
  },
  watch: {
    value: {
      immediate: true,
      handler(changedSteps) {
        this.steps = changedSteps;
      },
    },
  },
  methods: {
    addEmptyStep() {
      this.steps.push("");
      this.notifyObservers();
    },
    deleteStepByIndex(index) {
      this.steps.splice(index, 1);
      this.notifyObservers();
    },
    notifyObservers() {
      this.$emit("input", this.steps);
    },
  },
};
</script>
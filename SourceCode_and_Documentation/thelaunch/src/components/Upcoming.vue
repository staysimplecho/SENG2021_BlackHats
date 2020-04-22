<template>
  <div class="upcoming-wrap">
    <v-expansion-panels accordion focusable flat hover>
      <v-expansion-panel v-for="(item, i) in 5" :key="i">
        <v-expansion-panel-header expand-icon="mdi-chevron-down"
          >Item</v-expansion-panel-header
        >
        <v-expansion-panel-content>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      default() {
        return 0;
      },
    },
    name: {
      type: String,
      default() {
        return "Black On Black";
      },
    },
    day: {
      type: String,
      default() {
        return "Wed";
      },
    },
    date: {
      type: String,
      default() {
        return "01 Apr";
      },
    },
    time: {
      type: String,
      default() {
        return "9:00PM";
      },
    },
  },
};
</script>

<style scoped>
.upcoming-wrap {
  width: 100%;
}
</style>

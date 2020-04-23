<template>
  <div id="calendar-wrap">
    <full-calendar :events="fcEvents" locale="en"></full-calendar>
  </div>
</template>

<script>
var demoEvents = [
  {
    title: "Sunny Out of Office",
    start: "2016-08-25",
    end: "2017-07-27",
  },
];
export default {
  data() {
    return {
      fcEvents: demoEvents,
    };
  },
  components: {
    "full-calendar": require("vue-fullcalendar"),
  },
};
</script>

<style lang="scss" scoped>
#calendar-wrap{
  .comp-full-calendar.full-calendar-header.header-center.title {
    background-color: white !important;
  }
}
</style>

<template>
  <div id="artist-page">
    <Header></Header>

    <Footer></Footer>
    <Player></Player>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import Player from "@/components/Player.vue";
// import axios from "axios";

export default {
  name: "EventPage",
  components: {
    Header,
    Footer,
    Player,
  },
  data() {
    return {
      event: {
        id: -1,
      },
    };
  },
  methods: {
    getEventInfo() {
      this.event.id = this.$route.params.id;
      this.url = require("../assets/artists/img/" + this.event.id + ".jpg");
      //axios get info
    },
  },

  mounted() {
    this.getEventInfo();
  },
};
</script>

<style lang="scss"></style>

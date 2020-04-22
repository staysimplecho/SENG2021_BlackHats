<template>
  <div id="event-page">
    <Header></Header>
    <div class="container">
      <div class="main-info">
        <div class="date"></div>
      </div>
      <div class="event-img">
        <img :src="url" width="800px" height="500px" />
      </div>
      <div class="time-locate"></div>
      <div class="comments"></div>
    </div>
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
      url: "",
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

<style scoped lang="scss">
#event-page {
  background-image: linear-gradient(
    rgb(0, 0, 0) 25%,
    rgba(27, 27, 27, 3) 25%,
    rgb(27, 27, 27) 75%,
    black 75%
  );
  .container {
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(3, 1fr);
    grid-template-areas:
      "main-info"
      "time-locate"
      "comments";
    .main-info {
      grid-area: main-info;
      background-color: #a0f;
      .date {
        color: white;
      }
    }
    .time-locate {
      grid-area: time-locate;
      background-color: #fff;
    }
    .comments {
      grid-area: comments;
      background-color: #122;
    }
  }
}
</style>

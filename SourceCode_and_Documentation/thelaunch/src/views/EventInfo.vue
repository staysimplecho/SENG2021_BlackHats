<template>
  <div id="event-page">
    <Header></Header>
    <div class="event-info">
      <div class="event-info_timelocation">
        {{ event.day + ", " + event.date + " | " + event.location }}
      </div>
      <div class="event-info_artist">{{ event.name }}</div>
      <div class="event-info_description">{{ event.description }}</div>
      <button class="event-info_btn" @click="toTicketPage()">BOOK NOW</button>
      <img class="event-info_img" :src="url" />
      <div class="event-info_extend">
        <div class="event-info_extend_title">Time & Location</div>
        <div class="event-info_extend_time">
          {{ event.date + ", " + event.time }}
        </div>
        <div class="event-info_extend_location">
          {{ event.location + ", " + event.lo_precise }}
        </div>
      </div>
      <!-- Google Map -->
      <div class="map-home">
        <div></div>
        <GmapMap
          :center="center"
          :zoom="15"
          style="width: 900px; height: 480px; margin-left:80px; margin-right:80px;"
        >
          <GmapMarker
            :key="index"
            v-for="(m, index) in markers"
            :position="m.position"
            :clickable="true"
            @click="openWindow"
          />
          <gmap-info-window
            @closeclick="window_open = false"
            :opened="window_open"
            :position="infowindow"
          >
            <b>Home</b>
          </gmap-info-window>
        </GmapMap>
      </div>
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
      url: "",
      event: {
        id: 4,
        name: "Enamour",
        day: "Thu",
        date: "23 Apr",
        time: "3:00AM GMT+10",
        location: "Streaming LIVE",
        lo_precise: "Online Platform",
        description:
          "As a curator of infectious grooves and wistful atmospheres, Enamour has developed a sound that delicately walks the line between deep introspection and pure club play. His sets are an intricate blend of deep, progressive, tech house and techno that values musicality over anything else.",
      },
      //maps
      center: { lat: -33.9435913, lng: 151.2219017 },
      markers: [
        {
          position: { lat: -33.9435913, lng: 151.2219017 },
        },
      ],
      infowindow: { lat: -33.9425913, lng: 151.2219017 },
      window_open: false,
    };
  },
  methods: {
    getEventInfo() {
      this.event.id = this.$route.params.id;
      this.url = require("../assets/events/" + this.event.id + "_large.jpg");
      //axios get info
    },
    openWindow() {
      this.window_open = true;
    },
    toTicketPage() {
      window.open(
        "https://www.bandsintown.com/t/102190707?app_id=1640370bd8cf5d04b5b855b801530c46&came_from=267&utm_medium=api&utm_source=public_api&utm_campaign=ticket",
        "_blank"
      );
    },
  },

  mounted() {
    this.getEventInfo();
  },
};
</script>

<style lang="scss" scoped>
#event-page {
  .event-info {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    &_timelocation {
      color: white;
      width: 560px;
      font-size: 18px;
      font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
    }
    &_artist {
      color: white;
      margin-bottom: 20px;
      width: 560px;
      font-size: 60px;
      font-family: "Anton", sans-serif;
    }
    &_description {
      color: white;
      margin-bottom: 40px;
      width: 560px;
      font-size: 16px;
      font-weight: bold;
      font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
    }
    &_btn {
      outline: none;
      margin-bottom: 40px;
      width: 170px;
      height: 50px;
      border: solid #fc9779 2px;
      color: #fc9779;
      font-size: 14px;
      font-weight: bold;
      font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
    }
    &_img {
      margin-bottom: 40px;
      width: 980px;
      height: 400px;
    }
    &_extend {
      color: white;
      margin-bottom: 40px;
      width: 900px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      &_title {
        margin: 20px 0px;
        font-size: 30px;
        font-family: "Anton", sans-serif;
      }
      &_time,
      &_location {
        margin-bottom: 5px;
        font-size: 16px;
        font-weight: bold;
        font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
      }
    }
  }
}
</style>

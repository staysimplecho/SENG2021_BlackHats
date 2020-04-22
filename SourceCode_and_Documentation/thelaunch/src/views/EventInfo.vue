<template>
  <div id="event-page">
    <Header></Header>
    <div class="event-info">
      <div class="event-info_timelocation">
        {{ event.day + ", " + event.date + " | " + event.location }}
      </div>
      <div class="event-info_artist">{{ event.name }}</div>
      <div class="event-info_description">{{ event.description }}</div>
      <button class="event-info_btn">BOOK NOW</button>
      <img class="event-info_img" src="../assets/artists/test.jpg" />
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
            <b>UNSW</b>
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
      event: {
        id: 0,
        name: "The Sunday Brunches",
        day: "Sat",
        date: "21 Mar",
        time: "7:30PM",
        location: "ivy Den, Lounge & Terrace",
        lo_precise: "Level 2/330 George St, Sydney NSW 2000, Australia",
        description:
          "I’m an event description. To edit the event description go to My Events. Simply click Manage Events and start editing your event details. I’m a great place to get your guests excited by telling them a little more about your upcoming events.",
      },
      //maps
      center: { lat: -33.8665297, lng: 151.2069201 },
      markers: [
        {
          position: { lat: -33.8665297, lng: 151.2069201 },
        },
      ],
      infowindow: { lat: -33.916, lng: 151.22884 },
      window_open: false,
    };
  },
  methods: {
    getEventInfo() {
      this.event.id = this.$route.params.id;
      this.url = require("../assets/artists/" + this.event.id + ".jpg");
      //axios get info
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
    color: white;
    text-align: center;
    &_timelocation {
      width: 560px;
      font-size: 18px;
      font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
    }
    &_artist {
      margin-bottom: 20px;
      width: 560px;
      font-size: 60px;
      font-family: "Anton", sans-serif;
    }
    &_description {
      margin-bottom: 40px;
      width: 560px;
      font-size: 16px;
      font-weight: bold;
      font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
    }
    &_btn {
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

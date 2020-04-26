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
      <!--update start here-->
      <div class="share">
        <div>
          <h3
            style="color: white; font-size:30px;font-weight:bold; font-family: anton, sans-serif;margin-left:-500px;margin-top:40px;"
          >
            Share This Event
          </h3>
        </div>
        <div class="sharelink" style="margin-left:-650px;margin-top:20px;">
          <a
            href="https://www.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Foh0917ce.wixsite.com%252Fthelaunch%252Fevents%252Fblack-on-black%26title%3DBlack%2Bon%2BBlack&cancel_url=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=en_GB"
            target="_blank"
          >
            <svg viewBox="0 0 9 16" fill="currentColor" width="9" height="16">
              <path
                d="M5.39324257,16 L5.39324257,8.70173788 L7.84309113,8.70173788 L8.20960391,5.85761755 L5.39324257,5.85761755 L5.39324257,4.04152086 C5.39324257,3.21816097 5.62190137,2.65686476 6.80283471,2.65686476 L8.30887758,2.65639427 L8.30887758,0.112447437 C8.04822537,0.077631076 7.15429176,0 6.11450584,0 C3.94271768,0 2.45596495,1.32584468 2.45596495,3.75969653 L2.45596495,5.85761755 L-1.0658141e-13,5.85761755 L-1.0658141e-13,8.70173788 L2.45596495,8.70173788 L2.45596495,16 L5.39324257,16 Z"
                fill="#fff"
                fill-rule="evenodd"
              ></path>
            </svg>
          </a>
          <a href="https://twitter.com/login" target="_blank" style="margin-left: 20px;">
            <svg viewBox="0 0 18 14" fill="currentColor" width="18" height="14">
              <path
                d="M50.0768084,18.6572894 C49.4120716,18.9383915 48.6969358,19.1284894 47.9467859,19.2134267 C48.7133818,18.7761005 49.3011937,18.0839623 49.5775926,17.2588567 C48.8603348,17.6638258 48.0677436,17.9575674 47.2215703,18.1158138 C46.5467537,17.4287314 45.5817448,17 44.5148767,17 C42.4676148,17 40.8070991,18.5824636 40.8070991,20.5340002 C40.8070991,20.8115633 40.8389301,21.0805316 40.902592,21.3388827 C37.8208235,21.1912535 35.0886652,19.7852371 33.2583844,17.6456249 C32.9390136,18.1694052 32.7565161,18.7761005 32.7565161,19.4242534 C32.7565161,20.6487667 33.411173,21.7312123 34.4064214,22.3657145 C33.7984499,22.3480192 33.2260229,22.187245 32.7257461,21.9243436 L32.7257461,21.9678235 C32.7257461,23.6807266 34.0037596,25.1094941 35.7014114,25.4330649 C35.3899984,25.5159799 35.0626699,25.5574374 34.7242006,25.5574374 C34.4849378,25.5574374 34.2520412,25.5362031 34.0265718,25.4947456 C34.4982007,26.8987397 35.867463,27.9210213 37.490312,27.9483226 C36.2213173,28.8967896 34.621811,29.4615218 32.884901,29.4615218 C32.5851593,29.4615218 32.2896618,29.4458488 32,29.4124806 C33.6414171,30.414539 35.5905335,31 37.6850114,31 C44.5074495,31 48.2364477,25.6155791 48.2364477,20.9440251 C48.2364477,20.7908346 48.2332646,20.637644 48.2268984,20.4869813 C48.9515835,19.98848 49.5813062,19.3656062 50.0768084,18.6572894"
                transform="translate(-32 -17)"
                fill="#fff"
                fill-rule="evenodd"
              ></path>
            </svg>
          </a>
          <a href="https://www.linkedin.com/login" target="_blank" style="margin-left: 20px;">
            <svg viewBox="0 0 19 16" fill="#fff" width="19" height="16">
              <path
                d="M2.30367607,0.025974026 C3.49850532,0.025974026 4.46947897,0.885212121 4.46947897,1.94130736 C4.46947897,2.99987879 3.49850532,3.85911688 2.30367607,3.85911688 C1.10464953,3.85911688 0.13647407,2.99987879 0.13647407,1.94130736 C0.13647407,0.885212121 1.10464953,0.025974026 2.30367607,0.025974026 L2.30367607,0.025974026 Z M0.433082736,15.9491169 L4.17287031,15.9491169 L4.17287031,5.31387879 L0.433082736,5.31387879 L0.433082736,15.9491169 Z M6.51467968,5.31325974 L10.0963692,5.31325974 L10.0963692,6.76554545 L10.1467367,6.76554545 C10.6448154,5.92983117 11.8634294,5.04830736 13.680857,5.04830736 C17.4612184,5.04830736 18.159368,7.25087879 18.159368,10.1158312 L18.159368,15.9484978 L14.427975,15.9484978 L14.427975,10.776974 C14.427975,9.54259307 14.4013922,7.95659307 12.4874268,7.95659307 C10.5426813,7.95659307 10.2460727,9.29992641 10.2460727,10.6865931 L10.2460727,15.9484978 L6.51467968,15.9484978 L6.51467968,5.31325974 Z"
                fill="#fff"
                fill-rule="evenodd"
              ></path>
            </svg>
          </a>
        </div>
      </div>
      <!--update end here-->
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

<template>
  <div id="home-wrap">
    <Header></Header>
    <!-- Top shows -->
    <div class="display-wrap">
      <el-carousel height="580px" width="100%">
        <el-carousel-item v-for="item in display" :key="item.id">
          <img :src="item.url" class="carousel_image_type" />
          <div class="info-wrap">
            <div class="artist">
              {{ item.name + "." }}
            </div>
            <div class="info-box">
              <div class="info-date">{{ item.date }}</div>
              <div class="info-time">{{ item.time }}</div>
              <div class="info-location">{{ item.location }}</div>
              <div class="info-button">
                <el-button @click="toEventPage(item.id)"
                  >GET TICKETS
                  <div class="arrow-bar">
                    <img
                      src="../assets/arrow.svg"
                      height="15px"
                      width="40px"
                    /></div
                ></el-button>
              </div>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>
    <!-- Upcoming events -->
    <div class="upcoming-title-wrap">
      <div class="upcoming-box">
        <div class="top-bar-wrap">
          <img src="../assets/white-bar.svg" height="3px" width="300px" />
        </div>
        <div class="blank"></div>
        <div class="upcoming-title">
          <div class="up-white">UPCOMING</div>
          <div class="sh-pink">
            &nbsp;SHOWS
            <span class="stripe-end" style="height:52px; width: 22px;"
              ><svg
                preserveAspectRatio="none"
                data-bbox="61.9 10.1 76.2 179.8"
                viewBox="61.9 10.1 76.2 179.8"
                height="52"
                width="22"
                xmlns="http://www.w3.org/2000/svg"
                data-type="shape"
                role="img"
                fill="black"
              >
                <g>
                  <path
                    d="M62 174.1l8.8 15.8h-4l-4.9-8.7v-7.1h.1zm0-11.1l14.9 26.8h4l-18.9-34v7.2zm0-18.1l25 45h4l-29-52.1v7.1zm0-18.1l35.1 63.1h4L62 119.7v7.1zm0-18.2l45.2 81.2h4L62 101.5v7.1zm0-18.1l55.3 99.4h4L62 83.4v7.1zm0-18.1l65.4 117.5h4L62 65.3v7.1zm0-18.2l75.5 135.6h.6v-6.1L62 47.1v7.1zm0-18.1l76 136.6v-7.1L62 29v7.1zM62 18l76 136.6v-7.1L62 10.9V18zm5.7-7.9L138 136.5v-7.1L71.6 10.1h-3.9zm10.1 0L138 118.3v-7.1L81.7 10.1h-3.9zm10.1 0l50.2 90.1v-7.1l-46.2-83h-4zm10.1 0l40.1 72V75L102 10.1h-4zm10.1 0L138 64v-7.1l-26-46.7h-3.9v-.1zm10.1 0L138 45.8v-7.1l-15.9-28.6h-3.9zm14 0h-4l9.8 17.6v-7.1l-5.8-10.5z"
                  ></path>
                </g>
              </svg>
            </span>
            <div class="btm-bar-wrap">
              <img src="../assets/white-bar.svg" height="7px" width="105px" />
            </div>
          </div>
        </div>
        <div class="blank"></div>
        <div class="block-border"></div>
        <div class="upcoming-subtitle">
          <div>All shows are 18+ to enter and 21+ to purchase alcohol.</div>
          <div>No smoking inside. Please bring a valid form of ID.</div>
        </div>
      </div>
    </div>
    <!-- Google Map -->
    <div class="map-home">
      <div></div>
      <GmapMap
        :center="center"
        :zoom="15"
        style="width: auto; height: 480px; margin-left:80px; margin-right:80px;"
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
    <!-- Upcoming Event list -->
    <Upcoming></Upcoming>
    <div class="btn-wrap">
      <div class="more-button">
        <el-button @click="toAllEvents()"
          >SEE MORE
          <div class="arrow-bar">
            <img src="../assets/arrow.svg" height="15px" width="40px" /></div
        ></el-button>
      </div>
    </div>
    <Footer></Footer>
    <Player></Player>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import Player from "@/components/Player.vue";
import Upcoming from "@/components/Upcoming.vue";

export default {
  name: "Home",
  components: {
    Header,
    Footer,
    Player,
    Upcoming,
  },
  data() {
    return {
      display: [
        {
          id: 1,
          name: "The Generator",
          date: "SUNDAY APR.4",
          time: "7:00PM",
          url: require("../assets/artists/1.jpg"),
          location: "FT. GOLDCOUNTRY",
        },
        {
          id: 2,
          name: "The Generator1",
          date: "SUNDAY APR.5",
          time: "8:00PM",
          url: require("../assets/artists/2.jpg"),
          location: "FT. GOLDCOUNTRY",
        },
        {
          id: 3,
          name: "The Generator2",
          date: "SUNDAY APR.6",
          time: "9:00PM",
          url: require("../assets/artists/3.jpg"),
          location: "FT. GOLDCOUNTRY",
        },
      ],
      //maps
      center: { lat: -33.91758, lng: 151.22884 },
      markers: [
        {
          position: { lat: -33.91758, lng: 151.22884 },
        },
      ],
      infowindow: { lat: -33.916, lng: 151.22884 },
      window_open: false,
    };
  },
  methods: {
    toEventPage(id) {
      this.$router.push({ name: "EventPage", params: { id: id } });
    },
    toAllEvents() {
      this.$router.push("/events");
    },
    openWindow() {
      this.window_open = true;
    },
  },
  mounted() {},
};
</script>

<style lang="scss">
// Your AWESOME styles go here
#home-wrap {
  background-color: black;
  //display wrap
  .display-wrap {
    position: relative;
    .carousel_image_type {
      width: 100%;
      position: absolute;
      top: 0;
      left: 0;
    }
    .info-wrap {
      overflow: visible;
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -70%);
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: center;
      .artist {
        line-height: 103px;
        width: 500px;
        word-wrap: normal;
        word-break: keep-all;
        color: #fc9779;
        font-size: 103px;
        font-family: "Anton", sans-serif;
      }
      .info-box {
        margin: 0px 120px;
        width: 300px;
        height: 285px;
        background-color: #fc9779;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
        overflow: visible;
        .info-date,
        .info-time,
        .info-location {
          white-space: nowrap;
          text-overflow: ellipsis;
          line-height: 45px;
          width: auto;
          margin: 2px 20px 2px 40px;
          background: black;
          color: white;
          font-family: "Anton", sans-serif;
          font-size: 35px;
          letter-spacing: 0.1em;
        }
        .info-button {
          button {
            z-index: 999;
            position: relative;
            margin: 20px 20px 2px 40px;
            height: 45px;
            outline: solid rgba(0, 0, 0, 1) 3px;
            background-color: transparent;
            border: none;
            border-radius: 0;
            color: black;
            font-family: "Avenir-LT-W01_85-Heavy1475544", sans-serif;
            .arrow-bar {
              position: absolute;
              z-index: -1;
              display: flex;
              flex-direction: row;
              align-items: center;
              width: 220px;
              height: 25px;
              background-color: white;
              top: calc((100% - 25px) * 0.5);
              right: 10px;
              img {
                margin-left: 30px;
              }
            }
            &:hover {
              color: #fc9779;
              background: black;
              background-color: black;
              .arrow-bar {
                width: 100px;
                right: 130px;
              }
            }
          }
        }
      }
    }
  }
  //upcoming-title-wrap
  .upcoming-title-wrap {
    margin-top: 30px;
    margin-bottom: 80px;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    .upcoming-box {
      width: 970px;
      display: grid;
      grid-template-rows: 3px 30px 93px 45px 45px 60px;
      .top-bar-wrap {
        justify-self: center;
        img {
          margin-bottom: 12px;
        }
      }
      .blank {
        background-color: transparent;
      }
      .upcoming-title {
        display: flex;
        flex-direction: row;
        align-items: center;
        color: black;
        line-height: 55px;
        font-size: 54px;
        letter-spacing: 0.04em;
        font-family: "Anton", sans-serif;
        .up-white {
          display: flex;
          align-items: center;
          justify-content: flex-end;
          background-color: #fff;
          height: 93px;
          width: 255px;
        }
        .sh-pink {
          display: flex;
          justify-content: space-between;
          background-color: #fc9779;
          height: 52px;
          width: 280px;
          padding-left: 20px;
          .stripe-end {
            float: right;
          }
          position: relative;
          .btm-bar-wrap {
            position: absolute;
            bottom: -12px;
            right: 0;
          }
        }
      }
      .block-border {
        border-style: none solid solid none;
        border-width: 2px;
        border-color: #fc9779;
      }
      .upcoming-subtitle {
        margin-top: 30px;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        div {
          margin: 3px 0px;
          color: black;
          background: #fc9779;
          width: auto;
          font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
          font-size: 16px;
          letter-spacing: 0.03em;
        }
      }
    }
  }

  // Google Map
  .map-home {
    margin-bottom: 50px;
  }

  // more button
  .btn-wrap {
    width: 100%;
    display: flex;
    justify-content: center;
    margin-bottom: 30px;
    .more-button {
      width: 230px;
      height: 66px;
      background-color: #fc9779;
      display: flex;
      align-items: center;
      button {
        z-index: 999;
        position: relative;
        margin-left: 20px;
        height: 45px;
        width: 140px;
        outline: solid rgba(0, 0, 0, 1) 3px;
        background-color: transparent;
        border: none;
        border-radius: 0;
        color: black;
        font-family: "Avenir-LT-W01_85-Heavy1475544", sans-serif;
        .arrow-bar {
          position: absolute;
          z-index: -1;
          display: flex;
          flex-direction: row;
          align-items: center;
          width: 220px;
          height: 25px;
          background-color: white;
          top: calc((100% - 25px) * 0.5);
          right: 10px;
          img {
            margin-left: 30px;
          }
        }
        &:hover {
          color: #fc9779;
          background: black;
          background-color: black;
          .arrow-bar {
            width: 90px;
            right: 140px;
          }
        }
      }
    }
  }
}
</style>

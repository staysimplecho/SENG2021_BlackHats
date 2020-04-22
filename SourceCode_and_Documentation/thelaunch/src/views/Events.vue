<template>
  <div id="shows-wrap">
    <Header></Header>
    <div class="content-wrap">
      <div class="list-title">
        <div class="up-white">CALENDAR</div>
        <div class="sh-pink">
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
      <div class="list-content">
        <div class="card-wrap" v-for="event in 10" :key="event.id">
          <EventCard
            :id="event.id"
            :name="event.name"
            :day="event.day"
            :date="event.date"
            :time="event.time"
            :location="event.location"
            :description="event.description"
          ></EventCard>
        </div>
      </div>
    </div>
    <Footer></Footer>
    <Player></Player>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import EventCard from "@/components/EventCard.vue";
import Footer from "@/components/Footer.vue";
import Player from "@/components/Player.vue";

export default {
  name: "Shows",
  components: {
    Header,
    EventCard,
    Footer,
    Player,
  },
  data() {
    return {
      events: [],
    };
  },
  methods: {
    getEvents() {},
  },
};
</script>

<style lang="scss">
#shows-wrap {
  .content-wrap {
    width: 100%;
    display: grid;
    grid-template-columns: 460px auto 460px;
    grid-template-rows: 200px auto;
    .list-title {
      grid-column: 2;
      grid-row: 1;
      align-self: center;
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
        justify-content: flex-end;
        background-color: #fc9779;
        height: 52px;
        width: 250px;
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
    .list-content {
      grid-row: 2;
      grid-column: 2;
      justify-self: center;
      margin: 0;
      padding: 0;
      width: 890px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: flex-start;
      min-height: 100vh;
      background: transparent;
      .card-wrap {
        margin: 30px 0px;
      }
    }
  }
}
</style>

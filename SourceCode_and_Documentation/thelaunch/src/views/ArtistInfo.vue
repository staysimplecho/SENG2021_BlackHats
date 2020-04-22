<template>
  <div id="artist-page">
    <Header></Header>
    <div class="info-wrap">
      <div class="ar-photo">
        <img :src="url" width="240px" height="240px" />
      </div>
      <div class="ar-link"></div>
      <div class="ar-info">
        <div class="info-name">{{ this.artist.name }}</div>
        <div class="info-genre">{{ this.artist.genre }}</div>
        <div class="info-description">{{ this.artist.description }}</div>
      </div>
    </div>
    <div class="events-wrap">
      <el-table :data="events" style="width: 100%" stripe>
        <el-table-column label="" width="125">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.date }}</span>
          </template>
        </el-table-column>
        <el-table-column label="" width="595">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{
              scope.row.location + "    " + scope.row.area
            }}</span>
          </template>
        </el-table-column>
        <el-table-column label="">
          <template>
            <el-button @click="handleNotification()">Notify Me</el-button>
          </template>
        </el-table-column>
      </el-table>
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
  name: "Artists",
  components: {
    Header,
    Footer,
    Player,
  },
  data() {
    return {
      artist: {
        id: -1,
        name: "DJ Chili Fingers",
        genre: "House,Electronic",
        description:
          "Long Description crawled from artist's website/wiki.I'm a paragraph. Click here to add your own text and edit me. It’s easy. Just click “Edit Text” or double click me to add your own content and make changes to the font. I’m a great place for you to tell a story and let your users know a little more about you.",
      },
      url: "",
      events: [
        {
          date: "12 Nov",
          location: "The Venue",
          area: "San Francisco, CA",
        },
      ],
    };
  },
  methods: {
    getArtistInfo() {
      this.artist.id = this.$route.params.id;
      this.url = require("../assets/artists/img/" + this.artist.id + ".jpg");
      //axios get info
    },
    handleNotification() {},
  },

  mounted() {
    this.getArtistInfo();
  },
};
</script>

<style lang="scss">
#artist-page {
  .info-wrap {
    width: 100%;
    margin-top: 60px;
    display: grid;
    grid-template-columns: 520px 1fr 1fr 520px;
    grid-template-rows: 300px 100px;
    .ar-photo {
      grid-row: 1;
      grid-column: 2;
    }
    .ar-link {
      grid-row: 2;
      grid-column: 2;
    }
    .ar-info {
      grid-row: 1/3;
      grid-column: 3;
      display: flex;
      flex-direction: column;
      .info-name {
        font-size: 54px;
        color: #fc9779;
        font-family: "DINNeuzeitGroteskLTW01-_812426", sans-serif;
      }
      .info-genre {
        margin-top: 10px;
        font-size: 18px;
        color: #8394a0;
        font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
      }
      .info-description {
        margin-top: 30px;
        font-size: 14px;
        color: white;
        font-weight: bold;
        line-height: 1.6em;
        font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
      }
    }
  }
  .events-wrap {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    .el-table {
      width: 1000px !important;
    }
  }
}
</style>

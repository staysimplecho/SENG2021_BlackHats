<template>
  <div id="artist-page">
    <Header></Header>
    <div class="info-wrap">
      <div class="ar-photo">
        <img :src="url" width="240px" height="240px" />
      </div>
      <div class="ar-link">
        <button class="ar-btn">Preview Songs</button>
      </div>
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
            <span style="margin-left: 10px; font-size:16px;color:white;">{{
              scope.row.date
            }}</span>
          </template>
        </el-table-column>
        <el-table-column label="" width="155">
          <template slot-scope="scope">
            <span
              style="margin-left: 10px; font-size:16px; font-weight: bold;color:white;"
              >{{ scope.row.location }}</span
            >
          </template>
        </el-table-column>
        <el-table-column label="" width="440">
          <template slot-scope="scope">
            <span style="margin-left: 10px; font-size:16px;color:white;">{{
              scope.row.area
            }}</span>
          </template>
        </el-table-column>
        <el-table-column label="">
          <template slot-scope="scope">
            <el-button @click="handleNotification(scope.row.id)"
              >Notify Me</el-button
            >
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
  name: "ArtistPage",
  components: {
    Header,
    Footer,
    Player,
  },
  data() {
    return {
      artist: {
        id: 1,
        name: "Halsey",
        genre: "Pop, Electropop, Alternative Rock",
        description:
          "Ashley Nicolette Frangipane, known professionally as Halsey, \
          is an American singer and songwriter. Gaining attention from \
          self-released music on social media platforms, she was signed \
           by Astralwerks in 2014 and released her debut EP, Room 93, \
           later that year.",
      },
      url: "",
      events: [
        {
          date: "12 Nov",
          location: "The Venue",
          area: "San Francisco, CA",
        },
        {
          date: "12 Nov",
          location: "The Venue",
          area: "San Francisco, CA",
        },
        {
          date: "12 Nov",
          location: "The Venue",
          area: "San Francisco, CA",
        },
        {
          date: "12 Nov",
          location: "The Venue",
          area: "San Francisco, CA",
        },
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
      this.url = require("../assets/artists/" + this.artist.id + ".jpg");
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
    grid-template-rows: 250px 100px;
    .ar-photo {
      grid-row: 1;
      grid-column: 2;
    }
    .ar-link {
      grid-row: 2;
      grid-column: 2;
      .ar-btn {
        outline: none;
        width: 140px;
        height: 30px;
        background-color: transparent;
        color: white;
        border: solid white 2px;
        font-size: 16px;
        font-family: "DINNeuzeitGroteskLTW01-_812426", sans-serif;
        &:hover {
          border: none;
          color: #fc9779;
        }
      }
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
      .el-table__body tr.current-row > td {
        background-color: transparent !important;
      }
      width: 1000px !important;
      color: white;
      font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
      .cell {
        width: 100%;
        .el-button {
          background-color: transparent;
          margin-left: calc((100% - 200px) * 0.5) !important;
          width: 200px;
          border: solid white 2px;
          border-radius: 0;
          padding-left: 24px;
          font-size: 14px;
          color: white;
        }
      }
    }
  }
}
.el-table,
.el-table__expanded-cell {
  background-color: transparent !important;
}
.el-table th,
.el-table tr {
  background-color: transparent !important;
}

.el-table--striped,
.el-table__body tr.el-table__row--striped td {
  background-color: rgba(255, 255, 255, 0.2) !important;
}

.el-table--enable-row-hover,
.el-table__body tr:hover > td {
  background-color: transparent !important;
}
</style>

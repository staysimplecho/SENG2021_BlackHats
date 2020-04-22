<template>
  <div>
    <div id="header">
      <Header></Header>
    </div>

    <div class="container">
      <div class="title">
        <div>
          <h1>
            Latest News
          </h1>
        </div>
      </div>

      <div class="content">
        <div
          class="index-news"
          v-for="(article, index) in articles"
          :key="index"
          v-show="index < newsToShow"
        >
          <div class="border-line"></div>
          <div style="padding:20px;overflow:hidden;margin:0px 15%;">
            <section style="overflow:hidden;">
              <div class="news-title">
                <h2 style="inline-height:1.4em;font-size:20px;">
                  <span style="font-size:20px;">{{ article.title }}</span>
                </h2>
                <p style="font-size:12px; line-height=1.5em;">
                  <span style="font-size:12px;">
                    <span style="letter-spacing:0em;">{{
                      article.publishedAt | moment("MMM. DD, YYYY")
                    }}</span>
                  </span>
                </p>
              </div>
              <div class="news-detail">
                <p style="font-size:14px;line-height:1.6em;">
                  <span style="font-size:14px;">
                    <span
                      v-if="article.description"
                      style="letter-spacing:0.01em;"
                    >
                      {{ article.description }}
                    </span>
                    <span v-else
                      >There is not a short description for this news. Click
                      "Read More" to get more information.</span
                    >
                  </span>
                </p>
                <div>
                  <a :href="article.url" target="_blank">
                    <span style="margin-left:0px;">Read More</span>
                  </a>
                </div>
              </div>
              <div class="news-img">
                <a style="cursor:pointer;" :href="article.url" target="_blank">
                  <picture :src="article.url">
                    <img
                      v-if="article.urlToImage"
                      style="object-position:50% 50%;object-fit:cover;"
                      itemprop="image"
                      :src="article.urlToImage"
                    />
                    <span v-else>
                      <span style="position:absolute;margin-left:80px;margin-top:60px;"><u>No picture provided.</u></span>
                      <br>
                      <span style="position:absolute;margin-left:40px;margin-top:70px;"><u>Click link to see more information.</u></span>
                    </span>
                  </picture>
                </a>
              </div>
            </section>
          </div>
        </div>
        <div class="loading">
          <button v-if="showMore" @click="loadMore">
            <span>Load More</span>
          </button>
          <span class="nomore" v-else>There is no more news</span>
        </div>
      </div>
    </div>

    <div id="footer">
      <Footer></Footer>
    </div>
    <Player></Player>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import Player from "@/components/Player.vue";
import axios from "axios";
import Vue from "vue";
Vue.use(require("vue-moment"));
export default {
  name: "News",
  components: {
    Header,
    Footer,
    Player,
  },
  data() {
    return {
      articles: [],
      newsToShow: 5,
      totalNews: 20,
      showMore: true,
      totalResults: 0,
    };
  },
  mounted() {
    axios
      .get(
        "https://newsapi.org/v2/top-headlines?category=entertainment&country=au&apiKey=78ea33945cae4f97908a86b821880b8f"
      )
      .then((response) => {
        this.articles = response.data.articles;
        this.totalResults = response.data.totalResults;
        console.log(this.totalResults);
        console.log(this.articles);
      });
  },
  methods: {
    loadMore() {
      if (this.newsToShow < this.totalNews) {
        this.newsToShow += 5;
      } else {
        this.showMore = false;
      }
    },
  },
};
</script>

<style scoped lang="scss">
// Your AWESOME styles go here
#news-wrap {
  background-color: black;
}
// contact-middle
.container {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 130px 1fr 100px;
  grid-template-areas:
    "title"
    "content"
    "loading";
  .title {
    grid-area: title;
    background-color: #000000;
    h1 {
      text-align: center;
      font: normal normal normal 54px/1.4em dinneuzeitgroteskltw01-_812426,
        sans-serif;
      color: #fc9779;
    }
  }
  .content {
    grid-area: content;
    background-color: #000;
    .index-news {
      width: 100%;
      padding: 80px 0px;
      background-color: #000;
      overflow: hidden;
      height: auto;
      min-height: 280px;
      .news-title {
        float: left;
        width: 28%;
        h2 {
          font: normal normal normal 54px/1.4em anton, sans-serif;
          color: #ffffff;
        }
        p {
          font: normal normal bold 14px/1.4em avenir-lt-w01_35-light1475496,
            sans-serif;
          color: #ffffff;
        }
      }
      .news-detail {
        float: left;
        width: 35%;
        margin: 0px 2%;
        p {
          font: normal normal bold 14px/1.4em avenir-lt-w01_35-light1475496,
            sans-serif;
          color: #ffffff;
        }
        a {
          span {
            font: normal normal 700 14px/1.4em poppins-extralight, poppins,
              sans-serif;
            transition: color 0.4s ease 0s;
            color: #fc9779;
            white-space: nowrap;
            display: inline-block;
          }
          span:hover {
            color: #7e4c3d;
            transition: color 0.4s ease 0s;
          }
        }
      }
      .news-img {
        float: left;
        width: 240px;
        height: 200px;
        background-color: #ccc;
        /*background-image: url("");*/
        a {
          display: block;
          overflow: hidden;
          picture {
            width: 240px;
            height: 200px;
            img {
              width: 240px;
              height: 200px;
            }
          }
        }
      }
    }
    .loading {
      grid-area: loading;
      display: flex;
      justify-content: center;
      button {
        box-sizing: border-box;
        width: 100px;
        height: 50px;
        border: 3px double white;
        background-color: #fc9779;
        outline: none;
        span {
          font-size: 15px;
          font-family: sans-serif;
        }
      }
      button:hover {
        background-color: black;
        border: 3px double #fc9779;
        span {
          color: #fc9779;
        }
      }
      .nomore {
        font-size: 20px;
        font-weight: bold;
        font-family: sans-serif;
        color: #fc9779;
      }
    }
  }
}
.border-line {
  margin: 0px 14%;
  box-sizing: border-box;
  border: 1px solid rgba(27, 27, 27, 1);
  height: 0;
}
</style>

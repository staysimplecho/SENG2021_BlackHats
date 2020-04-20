<template>
  <div>
    <div id="header">
      <Header></Header>
    </div>

    <div class="container">
      <div class="title">
        <div>
          <h1 id="big-title">
            Latest News
          </h1>
        </div>
      </div>

      <div class="content">
        <div class="index-news">
          <div class="border-line"></div>
          <div style="padding:20px;overflow:hidden;margin:0px 20%;">
            <article>
              <div class="news-title">
                <h2
                  class="title-font"
                  style="inline-height:1.4em;font-size:26px;"
                >
                  <span style="font-size:26px;">News Title 01</span>
                </h2>
                <p class="date-font" style="font-size:12px; line-height=1.5em;">
                  <span style="font-size:12px;">
                    <span style="letter-spacing:0em;">MAR. 23, 2020</span>
                  </span>
                </p>
              </div>
              <div class="news-detail">
                <p
                  class="detail-font"
                  style="font-size:14px;line-height:1.6em;"
                >
                  <span style="font-size:14px;">
                    <span style="letter-spacing:0em;">
                      I'm a paragraph. I'm connected to your collection through
                      a dataset. Click Preview to see my content. To update me,
                      go to the Data Manager.
                    </span>
                  </span>
                </p>
                <div>
                  <!--change link-->
                  <a
                    href="https://www.youtube.com/watch?v=cQAXMjxh04I"
                    target="_self"
                  >
                    <span
                      @mouseover="hover1 = true"
                      @mouseleave="hover1 = false"
                      :class="{ active: hover1 }"
                      class="readmore-font"
                      style="margin-left:0px;"
                      >Read More</span
                    >
                  </a>
                </div>
              </div>
              <div class="news-img">
                <!--change link-->
                <a
                  style="cursor:pointer; width:250px;height:129px;"
                  href="https://www.youtube.com/watch?v=cQAXMjxh04I"
                  target="_self"
                  class="ca1link"
                >
                  <picture
                    style="width:250px;height:129px;"
                    src="https://static.wixstatic.com/media/fc7570_e715f827b1bd4242ac856f8c3193188d~mv2_d_5472_3648_s_4_2.jpg/v1/fill/w_500,h_258,al_c,q_80,usm_0.66_1.00_0.01/heidi-sandstrom-362642-unsplash.webp"
                  >
                    <img
                      style="object-position:50% 50%;width:250px;height:129px;object-fit:cover;"
                      itemprop="image"
                      src="https://static.wixstatic.com/media/fc7570_e715f827b1bd4242ac856f8c3193188d~mv2_d_5472_3648_s_4_2.jpg/v1/fill/w_500,h_258,al_c,q_80,usm_0.66_1.00_0.01/heidi-sandstrom-362642-unsplash.webp"
                    />
                  </picture>
                </a>
              </div>
            </article>
          </div>
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

export default {
  name: "News",
  components: {
    Header,
    Footer,
    Player
  },
  data() {
    return {
      hover1: false,
      hover2: false,
      hover3: false,
      hover4: false,
      hover5: false,
      hover6: false,
    };
  },
};
</script>

<style scoped lang="scss">
// Your AWESOME styles go here
#news-wrap {
  background-color: black;
}
#big-title {
  text-align: center;
  font: normal normal normal 54px/1.4em dinneuzeitgroteskltw01-_812426,
    sans-serif;
  color: #fc9779;
}
// contact-middle
.container {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 200px 1fr;
  grid-template-areas:
    "title"
    "content";
}
.container > .title {
  grid-area: title;
  background-color: #000000;
}
.container > .content {
  grid-area: content;
  background-color: #000;
}
.news-title {
  float: left;
  width: 28%;
}
.title-font {
  font: normal normal normal 54px/1.4em anton, sans-serif;
  color: #ffffff;
}
.date-font {
  font: normal normal bold 14px/1.4em avenir-lt-w01_35-light1475496, sans-serif;
  color: #ffffff;
}
.news-detail {
  float: left;
  width: 35%;
  margin: 0px 2%;
}
.detail-font {
  font: normal normal bold 14px/1.4em avenir-lt-w01_35-light1475496, sans-serif;
  color: #ffffff;
}
.readmore-font {
  font: normal normal 700 14px/1.4em poppins-extralight, poppins, sans-serif;
  transition: color 0.4s ease 0s;
  color: #fc9779;
  white-space: nowrap;
  display: inline-block;
}
.active {
  color: #7e4c3d;
  transition: color 0.4s ease 0s;
}
.news-img {
  float: left;
  width: 250px;
  height: 129px;
  background-color: rgb(235, 190, 191);
  /*background-image: url("");*/
}
.ca1link {
  display: block;
  overflow: hidden;
}
.border-line {
  margin: 0px 20%;
  box-sizing: border-box;
  border-top: 1px solid rgba(27, 27, 27, 1);
  height: 0;
}
.index-news {
  width: 100%;
  padding: 80px 0px;
  background-color: #000;
  overflow: hidden;
}
</style>

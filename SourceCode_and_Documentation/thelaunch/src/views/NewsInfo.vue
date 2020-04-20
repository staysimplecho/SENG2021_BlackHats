<template>
  <div>
    <div id="newsinfo-wrap">
      <Header></Header>
    </div>

    <div class="container">
      <section class="title">
        <div
          id="title-box"
          class="title-style"
          style="width:680px; pointer-events=none;"
        >
          <h1 class="title-font" style="line-height=1.4em;">News Title 01</h1>
        </div>
      </section>
      <section class="pics">
        <img
          style="position:relative;object-fit:cover;width:980px;height:560px;"
          src="https://static.wixstatic.com/media/fc7570_e715f827b1bd4242ac856f8c3193188d~mv2_d_5472_3648_s_4_2.jpg/v1/fill/w_1960,h_1120,al_c,q_90,usm_0.66_1.00_0.01/heidi-sandstrom-362642-unsplash.webp"
        />
      </section>

      <section class="article">
        <article>
          <div style="min-height:14px; width:111px;overflow:hidden;">
            <p
              class="article-font"
              style="position:relative;top:15px;font-size:14px;line-height:1.6em;"
            >
              <span style="font-weight:bold;">
                <span style="font-size:14px;">FULL NAME</span>
              </span>
            </p>
          </div>
          <div style="min-height:14px;width:100px; overflow:hidden;">
            <p
              class="article-font"
              style="position:relative;font-size:14px;line-height:1.6em;"
            >
              <span style="font-size:14px;">Mar, 23, 2020</span>
            </p>
          </div>
          <div
            style="width: 680px; min-height: 88px; pointer-events: none;overflow:hidden;"
          >
            <p class="article-font;font-size:26px;line-height:1.4em;">
              <span style="font-weight:bold;">
                <span style="font-size:26px;">
                  <span
                    style="font-family:poppins-extralight,poppins,sans-serif;color:#ffffff;"
                  >
                    I'm a paragraph. I'm connected to your collection through a
                    dataset. Click Preview to see my content. To update me, go
                    to the Data Manager.
                  </span>
                </span>
              </span>
            </p>
          </div>
          <div style="width=680px;min-height:323px; pointer-events:none;">
            <p class="article-font" style="font-size:18px;line-height:1.6em;">
              <span style="font-size:18px;"
                >I'm a paragraph. I'm connected to your collection through a
                dataset. To update me, go to the Data Manager. The Data Manager
                is where you store data to use in your site pages, or collect
                data from site visitors when they submit a form. This collection
                in the Data Manager is already set up with some fields and
                content. To customize it with your own content, you can import a
                CSV file or simply edit the placeholder text. You can also add
                more fields which you can connect to other page elements so the
                content displays on your published site. Remember to sync the
                collection so your content is live! You can add as many new
                collections as you need to store or collect data. With Presets,
                we’ve handled the page set up for you, but you can create the
                exact same functionality in your other site pages. To connect
                page elements to data, the first step is to add a dataset to the
                page and choose the collection you want to use. From the dataset
                Settings panel, you can filter or sort the available items,
                decide how your users can interact with the page (read/write),
                and more. Next, select the element you want to connect to the
                data, and choose the field you want to connect it to. So simple!
                If you want to add even more capabilities, enable Developer
                Tools to use JavaScript and APIs to add custom interactions and
                functionality to your site. To see what’s possible and get
                answers to your questions, check out the Wix Code Forum.</span
              >
            </p>
          </div>
        </article>
      </section>
      <!--<section class="page-nav">
        <div
          style="height:40px;min-height:22px;width:132px; z-index=-1;"
          role="button"
        >
          <button class="g-transparent-a page-nav-style" type="button" disabled>
            <span class="page-nav-animation" style="margin-left:0px;"
              >Previous News</span
            >
          </button>
        </div>
        <div>
          <a href="#" class="next">Next &raquo;</a>
        </div>
      </section>-->
      <!--<section class="page-nav">
        <ul class="pager">
          <li class="previous disabled"><span style="font-size:18px;">&laquo; Previous</span></li>
          <li class="next"><a href="#" style="font-size:18px;">Next &raquo;</a></li>
        </ul>
      </section>-->
      <section class="page-nav">
        <div
          v-for="newsPage in visiblePages"
          :visiblePages="visiblePages"
          :currentPage="currentPage"
          :newsPage="newsPage"
          :key="newsPage.id"
        ></div>
        <div v-on:click="addNewsPage"></div>
        <Pagination
          style="color:white;"
          v-bind:newsPages="newsPages"
          v-on:page:update="updatePage"
          v-bind:currentPage="currentPage"
          v-bind:pageSize="pageSize"
        >
        </Pagination>
      </section>
    </div>
    <div id="newsinfo-wrap">
      <Footer></Footer>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import Pagination from "@/views/Pagination.vue";
export default {
  name: "NewsInfo",
  components: {
    Header,
    Footer,
    Pagination,
  },
  data() {
    return {
      newsPages: [
        {
          id: 1,
          link: "https://oh0917ce.wixsite.com/thelaunch/News/News-Title-01",
        },
        {
          id: 2,
          link: "https://oh0917ce.wixsite.com/thelaunch/News/News-Title-02",
        },
        {
          id: 3,
          link: "https://oh0917ce.wixsite.com/thelaunch/News/News-Title-03",
        },
        {
          id: 4,
          link: "https://oh0917ce.wixsite.com/thelaunch/News/News-Title-04",
        },
        {
          id: 5,
          link: "https://oh0917ce.wixsite.com/thelaunch/News/News-Title-05",
        },
        {
          id: 6,
          link: "https://oh0917ce.wixsite.com/thelaunch/News/News-Title-06",
        },
      ],
      nextId: 7,
      currentPage: 1,
      pageSize: 1,
      visiblePages: [],
    };
  },
  beforeMount: function() {
    this.updateVisiblePages();
  },
  methods: {
    addNewsPage(link) {
      this.newsPages.push({ id: this.nextId, link: link });
      this.nextId++;
    },
    updatePage(pageNumber) {
      this.currentPage = pageNumber;
      this.updateVisiblePages();
    },
    updateVisiblePages() {
      this.visiblePages = this.newsPages.slice(
        this.currentPage * this.pageSize,
        this.currentPage * this.pageSize + this.pageSize
      );

      // if zero visiblePages, go back a page
      if (this.visiblePages.length == 0 && this.currentPage > 0) {
        this.updatePage(this.currentPage);
      }
    },
  },
};
</script>

<style lang="scss">
// Your AWESOME styles go here
#newsinfo-wrap {
  background-color: black;
}
.container {
  display: grid;
  grid-template:
    ". title ." 200px
    "pics pics pics" 560px
    ". article ." 1fr
    ". page-nav ." 60px
    / 1fr 680px 1fr;
  justify-content: center;
  align-content: center;
  background-color: #000;
}
.title {
  grid-area: title;
}
.title-font {
  font: normal normal normal 54px/1.4em dinneuzeitgroteskltw01-_812426,
    sans-serif;
  color: #fc9779;
}
#title-box {
  position: relative;
  margin: 44px 0px 45px calc((100% - 980px) * 0.5);
  left: 151px;
  //grid-area: 1 / 1 / 2 / 2;
  justify-self: start;
  align-self: start;
}
.title-style {
  word-wrap: break-word;
  text-align: start;
}
.title-style > * {
  pointer-events: auto;
}
.title-style h1 {
  margin: 0;
  line-height: normal;
  letter-spacing: normal;
}
.pics {
  grid-area: pics;
  overflow: hidden;
  justify-self: center;
}
.article {
  grid-area: article;
}
.article-font {
  font: normal normal bold 14px/1.4em avenir-lt-w01_35-light1475496, sans-serif;
  color: #ffffff;
}
.page-nav {
  grid-area: page-nav;
}
/*.page-nav-animation {
  font: normal normal normal 16px/1.4em poppins-extralight, poppins, sans-serif;
  transition: color 0.4s ease 0s;
  color: #ffffff;
  display: inline-block;
  margin: calc(-1 * 0px) 0px 0;
  position: relative;
  white-space: nowrap;
}
.g-transparent-a:link,
.g-transparent-a:visited {
  border-color: transparent;
}
.page-nav-style {
  border-radius: 0 0 0 0;
  position: relative;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  transition: border-color 0.4s ease 0s, background-color 0.4s ease 0s;
}
.page-nav-style {
  background-color: transparent;
  border: solid rgba(255, 255, 255, 1) 0px;
}
.page-nav-style:hover {
  background-color: transparent;
  border-color: transparent;
}
button.page-nav-style {
  width: 100%;
}*/
.pager {
  padding-left: 0;
  margin: 20px 0;
  text-align: center;
  list-style: none;
}
.pager li {
  display: inline;
  background-color: transparent;
  color: #fff;
  font: normal normal normal 16px/1.4em poppins-extralight, poppins, sans-serif;
}
.pager li > a,
.pager li > span {
  text-decoration: none;
  display: inline-block;
  padding: 5px 14px;
  background-color: transparent;
  color: #fff;
}
.pager li > a:focus,
.pager li > a:hover {
  text-decoration: none;
  background-color: transparent;
  color: white;
  border-color: transparent;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
  color: #fff;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > span {
  cursor: auto;
  background-color: transparent;
  border-color: transparent;
  color: grey;
}
.pager:after,
.pager:before {
  display: table;
  content: " ";
}
.pager:after {
  clear: both;
}
</style>

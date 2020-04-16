<template>
    <div>
        <div id="newsinfo-wrap">
            <Header></Header>
        </div>
        <div>
            <h1 class="title-font" style="line-height:1.4em">
                News Title 01
            </h1>
        </div>
        <div id="newsinfo-wrap">
            <Footer></Footer>
        </div>
    </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "NewsInfo",
  components: {
    Header,
    Footer,
  },
  data() {
    return {
    };
  },
};
</script>

<style lang="scss">
#newsinfo-wrap{
    background-color: black;
}
.title-font {
    font: normal normal normal 54px/1.4em dinneuzeitgroteskltw01-_812426,sans-serif;
    color:#FC9779;
}
</style>
<template>
  <div id="home-wrap">
    <Header></Header>
    <Footer></Footer>
    <Player></Player>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import Player from "@/components/Player.vue";

export default {
  name: "Home",
  components: {
    Header,
    Footer,
    Player
  },
};
</script>

<style lang="scss">
// Your AWESOME styles go here
#home-wrap {
  background-color: black;
}
</style>

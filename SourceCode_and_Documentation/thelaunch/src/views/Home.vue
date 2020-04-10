<template>
  <div id="home-wrap">
    <Header></Header>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/components/Header.vue";

export default {
  name: "Home",
  components: {
    Header,
  },
};
</script>

<style lang="scss">
// Your AWESOME styles go here
#home-wrap {
  background-color: black;
}
</style>

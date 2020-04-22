<template>
  <div id="card-wrap" @click="toThatArtist(id)">
    <div class="content-wrap">
      <div class="picture">
        <img :src="url" width="204px" />
      </div>
      <div class="name-block">
        <span>{{ name }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    name: String,
    id: Number,
  },
  data() {
    return {
      url: require("../assets/artists/img/" + this.id + ".jpg"),
    };
  },
  methods: {
    toThatArtist(id) {
      this.$router.push("/artists/" + id, { id: id });
    },
  },
};
</script>

<style lang="scss" scoped>
#card-wrap {
  width: 224px;
  background-color: black;
  display: flex;
  align-items: center;
  justify-content: center;
  .content-wrap {
    margin: 10px;
    width: 204px;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: transparent;
    .name-block {
      margin-top: -4px;
      width: 100%;
      height: 55px;
      background-color: #fff;
      text-align: end;
      line-height: 55px;
      color: black;
      font-size: 22px;
      font-family: "Impact-W02-2010", sans-serif;
      span {
        margin-right: 30px;
      }
    }
  }
}
</style>

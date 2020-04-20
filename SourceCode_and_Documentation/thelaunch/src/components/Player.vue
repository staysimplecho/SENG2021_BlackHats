<template>
  <transition>
    <div
      ref="dragIcon"
      class="dragIcon"
      :style="{
        left: left + 'px',
        top: top + 'px',
        width: itemWidth + 'px',
        height: itemHeight + 'px',
      }"
      v-if="isShow"
    >
      <span>
        <img src="../assets/default-track.png" height="40px" width="40px" />
      </span>
      <span class="play-button">
        <button class="play-pause" type="button">
          <svg
            v-if="!isPlaying"
            @click="isPlaying = !isPlaying"
            @mouseover="currentColor = '#fc9779'"
            @mouseout="currentColor = 'white'"
            width="20px"
            height="20px"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g :fill="currentColor">
              <path
                d="M17.29,9.02 C18.25,9.56 18.25,10.44 17.29,10.98 L1.74,19.78 C0.78,20.33 0,19.87 0,18.76 L0,1.24 C0,0.13 0.78,-0.32 1.74,0.22 L17.29,9.02 Z"
              ></path>
            </g>
          </svg>
          <svg
            v-if="isPlaying"
            @click="isPlaying = !isPlaying"
            @mouseover="currentColor = '#fc9779'"
            @mouseout="currentColor = 'white'"
            width="20px"
            height="20px"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g :fill="currentColor">
              <path
                d="m0,0.99c0,-0.55 0.45,-0.99 0.99,-0.99l4.02,0c0.55,0 0.99,0.46 0.99,0.99l0,18.02c0,0.55 -0.45,0.99 -0.99,0.99l-4.02,0c-0.55,0 -0.99,-0.46 -0.99,-0.99l0,-18.02zm10,0c0,-0.55 0.45,-0.99 0.99,-0.99l4.02,0c0.55,0 0.99,0.46 0.99,0.99l0,8.02c0,10.55 -0.45,10.99 -0.99,10.99l-4.02,0c-0.55,0 -0.99,-0.46 -0.99,-0.99l0,-18.02z"
              ></path>
            </g>
          </svg>
        </button>
      </span>
      <span class="music-info">
        <span class="track-name">{{ track }}</span>
        <span class="artist-name">{{ " - " + artist }}</span>
      </span>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      default: "test",
    },
    itemWidth: {
      type: Number,
      default: 320,
    },
    itemHeight: {
      type: Number,
      default: 40,
    },
  },
  data() {
    return {
      isPlaying: false,
      currentColor: "white",
      track: "Track Name",
      artist: "Artist Name",
      left: 0,
      top: 0,
      startToMove: false,
      isShow: true,
      timer: null,
      currentTop: null,
      clientW: document.documentElement.clientWidth, //window width
      clientH: document.documentElement.clientHeight, //window height
    };
  },
  created() {
    //    this.left = (this.clientW - this.itemWidth - 30)
    this.left = 0;
    this.top = this.clientH - this.itemHeight - 40;
  },
  mounted() {
    this.bindScrollEvent();
  },
  beforeDestroy() {
    this.removeScrollEvent();
  },
  methods: {
    bindScrollEvent() {
      window.addEventListener("scroll", this.handleScrollStart);
    },
    removeScrollEvent() {
      window.removeEventListener("scroll", this.handleScrollStart);
    },
    handleScrollStart() {
      this.isShow = false;
      this.timer && clearTimeout(this.timer);
      this.timer = setTimeout(() => {
        this.handleScrollEnd();
      }, 300);
      this.currentTop =
        document.documentElement.scrollTop || document.body.scrollTop;
    },
    handleScrollEnd() {
      this.scrollTop =
        document.documentElement.scrollTop || document.body.scrollTop;
      if (this.scrollTop == this.currentTop) {
        this.isShow = true;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.dragIcon {
  display: flex;
  flex-direction: row;
  position: fixed;
  width: 320px;
  height: 40px;
  background-color: black;
  line-height: 40px;
  color: #fff;
  .play-button {
    .play-pause {
      cursor: pointer;
      border: 0;
      margin: 10px 10px 10px 15px;
      padding: 0px;
      background-color: #000000;
      outline: none;
    }
  }
  .music-info {
    font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
    font-size: 13px;
    .artist-name {
      opacity: 0.6;
    }
  }
}
.v-enter {
  opacity: 1;
}
.v-leave-to {
  opacity: 0;
}
.v-enter-active,
.v-leave-active {
  transition: opacity 0.3s;
}
</style>

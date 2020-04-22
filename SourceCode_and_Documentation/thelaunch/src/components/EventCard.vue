<template>
  <div class="box">
    <div class="imgBx">
      <img :src="url" />
    </div>
    <div class="content">
      <h2>{{ name }}</h2>
      <h3>{{ day + ", " + date }}</h3>
      <h3>{{ time }}</h3>
      <p>{{ description }}</p>
    </div>
    <div class="btn">
      <el-button @click="toEventPage(id, name, day, date, time, description)"
        >Details</el-button
      >
    </div>
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: Number,
      default() {
        return 1;
      },
    },
    name: {
      type: String,
      default() {
        return "Black On Black";
      },
    },
    day: {
      type: String,
      default() {
        return "Wed";
      },
    },
    date: {
      type: String,
      default() {
        return "01 Apr";
      },
    },
    time: {
      type: String,
      default() {
        return "9:00PM";
      },
    },
    location: {
      type: String,
      default() {
        return "ivy Den, Lounge & Terrace";
      },
    },
    description: {
      type: String,
      default() {
        return "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.";
      },
    },
  },
  data() {
    return {
      url: require("../assets/artists/" + this.id + ".jpg")
    };
  },
  methods: {
    toEventPage(id, name, day, date, time, description) {
      this.$router.push({
        name: "EventPage",
        params: {
          id: id,
          name: name,
          day: day,
          date: date,
          time: time,
          description: description,
        },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.box {
  position: relative;
  width: 264px;
  height: 500px;
  background: #000;
  box-shadow: 0 30px 30px rgba(0, 0, 0, 0.5);
  .imgBx {
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    height: 55%;
    img {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: 0.5s;
    }
  }
  .content {
    position: absolute;
    bottom: 15%;
    left: 10%;
    width: 80%;
    height: 130px;
    background-color: transparent;
    color: white;
    transition: height 0.5s, ease-out 0.5s;
    overflow: hidden;
    padding: 10px;
    box-sizing: border-box;
    h2 {
      margin: 0;
      padding: 0;
      font-size: 28px;
      font-family: "Anton", sans-serif;
      letter-spacing: 0.03em;
      margin-bottom: 5px;
    }
    h3 {
      margin: 6px 0px 0px 0px;
      padding: 0;
      font-size: 16px;
      font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
      letter-spacing: 0.04em;
    }
    p {
      ::-webkit-scrollbar {
        width: 0 !important;
        height: 0;
      }
      -ms-overflow-style: none;
      overflow: -moz-hidden-unscrollable;
      margin: 10px 0 0;
      padding: 0;
      opacity: 0;
      line-height: 1.2em;
      text-align: justify;
    }
  }
  .btn {
    position: absolute;
    bottom: 0;
    height: 75px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    button {
      width: 160px;
      height: 42px;
      outline: none;
      background-color: transparent;
      border: solid #fc977f 2px;
      border-radius: 0;
      color: #fc9779;
      line-height: 14px;
      font-size: 14px;
      font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
      &:hover {
        filter: brightness(50%);
        transition: 0.4s;
      }
    }
  }
  &:hover {
    .imgBx img {
      opacity: 0;
    }
    .content {
      width: 80%;
      height: 85%;
      top: 0;
      left: 10%;
      p {
        opacity: 1;
      }
    }
  }
}
</style>

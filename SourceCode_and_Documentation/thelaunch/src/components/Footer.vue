<template>
  <div id="footer-wrap">
    <div class="subscribe-wrap">
      <div class="subscribe-box">
        <div class="subscribe-title">
          <p>STAY UP TO DATE</p>
        </div>
        <div class="stripe-wrap">
          <img src="../assets/stripe.svg" />
        </div>
        <div style="width: 100%; background-color: #fc9779;">
          <div
            style="height:100%; width: 426px; background-color: black;"
          ></div>
        </div>
        <div class="bg"></div>
        <div class="email-wrap">
          <p>
            With all the latest concerts and events. Sign up to get our
            newsletter
          </p>
          <div class="email-boxes">
            <el-form :inline="true" :model="form" class="demo-form-inline">
              <el-form-item>
                <el-input
                  v-model="form.email"
                  placeholder="Enter your email here*"
                ></el-input>
              </el-form-item>
              <el-form-item>
                <el-button @click="onSubmit">Subscribe </el-button>
              </el-form-item>
            </el-form>
          </div>
          <div class="outbound-bar">
            <img src="../assets/white-bar.svg" height="23px" width="223px" />
          </div>
        </div>
        <div class="bg"></div>
        <div class="bar-wrap">
          <img src="../assets/white-bar.svg" height="11px" width="390px" />
        </div>
      </div>
    </div>
    <div class="footer-text">
      LIVE LOCAL MUSIC, FOOD & DRINKS ©2020 BY BLACKHATS.
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email: "",
      },
    };
  },
  methods: {
    onSubmit() {
      console.log("submit!");
    },
  },
};
</script>

<style lang="scss">
#footer-wrap {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  background-color: transparent;
  .subscribe-wrap {
    .subscribe-box {
      width: 1080px;
      margin: 84px 0px 50px calc((100% - 1080px) * 0.5);
      display: grid;
      grid-template-rows: 14px 14px min-content min-content min-content 11px;
      position: relative;
      .subscribe-title {
        position: absolute;
        left: 54px;
        top: -35px;
        p {
          font-size: 54px;
          margin: 0px;
          color: white;
          letter-spacing: 0.005em;
          font-weight: 700;
          font-family: "Oswald" ,sans-serif;
        }
      }
      .stripe-wrap {
        justify-self: center;
        align-self: end;
        img {
          margin-bottom: -4px;
        }
      }
      .bg {
        height: 70px;
        width: 100%;
        background-color: #fc9779;
      }
      .email-wrap {
        background-color: #fc9779;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-evenly;
        position: relative;
        p {
          line-height: 1.6em;
          width: 333px;
          font-size: 14px;
          font-weight: bold;
          font-family: "Avenir-LT-W01_85-Heavy1475544", sans-serif;
          letter-spacing: 0.06em;
        }
        .email-boxes {
          z-index: 999;
          .el-form {
            display: flex;
            flex-direction: row;
            align-items: center;
            .el-form-item {
              margin-bottom: 0px;
              input {
                background-color: white;
                border-width: 3px;
                border-radius: 0;
                border-color: red;
                width: 425px;
                color: black;
                font-family: "Lato", sans-serif;
                letter-spacing: 0.06em;
              }
              ::placeholder {
                color: black;
                font-family: "Lato", sans-serif;
                letter-spacing: 0.06em;
              }
              button {
                outline: none;
                background-color: transparent;
                border: solid rgba(0, 0, 0, 1) 3px;
                border-radius: 0;
                color: black;
                font-weight: bold;
              }
            }
          }
        }
        .outbound-bar {
          z-index: 0;
          position: absolute;
          right: -50px;
          top: calc((100% - 23px) * 0.5);
        }
      }
      .bar-wrap {
        align-self: start;
        justify-self: start;
        img {
          margin-bottom: 3px;
        }
      }
    }
  }
  .footer-text {
    padding: 20px 0px 130px 0px;
    color: white;
    font-family: "Lato", sans-serif;
    text-align: center;
    font-size: 11px;
    letter-spacing: 0.3em;
    text-indent: 0.3em;
  }
}
</style>

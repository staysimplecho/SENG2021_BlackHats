<template>
  <div id="profile-wrap">
    <Header></Header>
    <div class="profile-container">
      <div class="profile-cards">
        <div class="profile-static">
          <div class="profile-static_avatar">
            <img src="../assets/user-icon-big.svg" width="71%" height="78%" />
          </div>
          <div class="profile-static_handle">oh0917ce</div>
          <div class="profile-static_follow">
            <div class="follower">
              <div class="follower-num">0</div>
              <div class="follower-text">Follower</div>
            </div>
            <div class="following">
              <div class="following-num">0</div>
              <div class="following-text">Following</div>
            </div>
          </div>
        </div>
        <div class="profile-options">
          <router-link class="option" to="/profile/account"
            >My Account</router-link
          >
          <router-link class="option" to="/profile/calendar"
            >Calendar</router-link
          >
        </div>
      </div>
      <div class="profile-content">
        <router-view></router-view>
      </div>
    </div>
    <Footer></Footer>
    <Player></Player>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Profile",
  components: {
    Header,
    Footer,
  },
  props: {
    id: {
      type: Number,
      default() {
        return 0;
      },
    },
  },
  methods: {
    toAccount() {
      this.$router.push(`/profile/account`);
      //   this.$router.push(`/profile/${this.id}/account`);
    },
    toCalendar() {
      this.$router.push(`/profile/calendar`);
      //   this.$router.push(`/profile/${this.id}/calendar`);
    },
  },
};
</script>

<style lang="scss">
// Your AWESOME styles go here
#profile-wrap {
  .profile-container {
    display: grid;
    grid-template-columns: 480px 300px auto 480px;
    .profile-cards {
      grid-column: 2;
      display: flex;
      flex-direction: column;
      align-items: center;
      .profile-static {
        border: solid rgba(128, 128, 128, 0.5) 1px;
        margin: 5px 0px;
        padding: 30px;
        width: 250px;
        height: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        &_avatar {
          display: flex;
          flex-direction: column;
          justify-content: flex-end;
          align-items: center;
          width: 90px;
          height: 90px;
          border-radius: 50%;
          background-color: rgba(128, 128, 128, 0.5);
        }
        &_handle {
          text-align: center;
          width: 100%;
          margin-top: 12px;
          color: white;
          font-size: 16px;
          font-weight: bold;
          font-family: "Avenir-LT-W01_35-Light1475496";
        }
        &_follow {
          width: 100%;
          margin-top: 25px;
          display: flex;
          justify-content: space-around;
          .follower,
          .following {
            color: white;
            text-align: center;
            width: 100%;
            font-weight: bold;
            font-family: "Avenir-LT-W01_35-Light1475496";
            &-num {
              font-size: 16px;
            }
            &-text {
              font-size: 12px;
              margin-top: 5px;
              opacity: 0.7;
            }
          }
          .follower {
            border-right: solid rgba(128, 128, 128, 0.5) 1px;
          }
        }
      }
      .profile-options {
        border: solid rgba(128, 128, 128, 0.5) 1px;
        margin: 5px 0px;
        width: 250px;
        height: auto;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        a {
          text-decoration: none;
        }
        a:-webkit-any-link {
          text-decoration: none !important;
        }
        .router-link-active {
          text-decoration: none;
        }
        .option {
          outline: none;
          color: white;
          font-size: 14px;
          font-weight: bold;
          font-family: "Avenir-LT-W01_35-Light1475496", sans-serif;
          margin: 15px 0px 15px 30px;
          &:hover {
            color: #8394a0;
          }
          &:active,
          &:focus {
            color: #fc9779;
          }
        }
      }
    }
    .profile-content {
      grid-column: 3;
    }
  }
}
</style>

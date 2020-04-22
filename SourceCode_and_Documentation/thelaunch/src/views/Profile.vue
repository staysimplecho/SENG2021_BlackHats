<template>
  <div id="profile-wrap">
    <Header></Header>
    <div class="profile-container">
      <div class="profile-cards">
        <div class="profile-static">
          <div class="profile-static_avatar">
              <img src="../assets/user-icon-big.svg" height="90" width="90"/>
          </div>
          <div class="profile-static_handle"></div>
          <div class="profile-static_follow"></div>
          <div class="profile-static_edit"></div>
        </div>
        <div class="profile-options"></div>
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
        height: 310px;
        display: flex;
        flex-direction: column;
        align-items: center;
        &_avatar {
            width: 90px;
            height: 90px;
            border-radius: 50%;
            background-color: rgba(0, 0, 0, 0.5);
        }
        &_handle {
        }
        &_follow {
        }
        &_edit {
        }
      }
      .profile-options {
        border: solid rgba(128, 128, 128, 0.5) 1px;
        margin: 5px 0px;
        width: 250px;
        height: 200px;
      }
    }
    .profile-content {
      grid-column: 3;
    }
  }
}
</style>

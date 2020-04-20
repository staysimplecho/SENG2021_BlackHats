<template>
  <div id="header-wrap">
    <div class="navigation">
      <router-link to="/"><p>HOME</p></router-link>
      <router-link to="/events"><p>SHOWS</p></router-link>
      <router-link to="/artists"><p>ARTISTS</p></router-link>
      <router-link to="/news"><p>NEWS</p></router-link>
      <router-link to="/contact"><p>CONTACT</p></router-link>
    </div>
    <div class="logo" @click="backHome()">
      <div class="logo-bold">THE</div>
      <div class="logo-main">
        LAUNCH
        <div class="bg-stripe"></div>
      </div>
      <div class="logo-sub">WHERE MUSIC MATTERS</div>
    </div>
    <div class="top-right">
      <div class="user-status" v-if="!loggedIn">
        <button @click="drawer = true">
          <div class="icon">
            <img src="../assets/user-icon.svg" />
          </div>
          <span>Sign Up | Log In</span>
        </button>
      </div>
      <div class="search">
        <el-input
          placeholder="Search..."
          suffix-icon="el-icon-search"
          v-model="input"
        >
        </el-input>
      </div>
    </div>
    <!-- popup Signup / Login -->
    <el-drawer
      title="我是外面的 Drawer"
      :visible.sync="drawer"
      size="100%"
      custom-class="login-popup"
    >
      <div>
        <el-button @click="innerDrawer = true" style="outline: none;"
          >打开里面的!</el-button
        >
        <el-drawer
          size="100%"
          custom-class="login-popup"
          title="我是里面的"
          :append-to-body="true"
          :visible.sync="innerDrawer"
        >
          <p>_(:зゝ∠)_</p>
        </el-drawer>
      </div>
    </el-drawer>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      loggedIn: false,
      drawer: false,
      innerDrawer: false,
      input: "",
    };
  },
  methods: {
    backHome() {
      this.$router.push({
        name: "Home",
      });
    },
  },
};
</script>

<style lang="scss">
#header-wrap {
  width: 100%;
  display: grid;
  grid-template-columns: 40px 400px auto 400px 40px;
  grid-template-rows: 40px auto 40px;
  background-color: transparent;
  .navigation {
    grid-column: 2;
    grid-row: 2;
    display: flex;
    flex-direction: row;
    a {
      text-decoration: none;
    }
    p {
      color: white;
      line-height: 17px;
      text-align: center;
      padding: 0 15px;
      margin: 0;
      font-size: 17px;
      letter-spacing: 0.03em;
      font-family: "Pathway Gothic One", sans-serif;
      &:hover {
        cursor: pointer;
        color: #fc9779;
        transition: all 0.6s ease;
      }
    }
  }
  .logo {
    cursor: pointer;
    grid-column: 3;
    grid-row: 2;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: auto;
    color: white;
    .logo-bold {
      padding-bottom: 6px;
      line-height: 20px;
      font-family: "Oswald", sans-serif;
      font-size: 20px;
      font-weight: 500;
      // recenter after change the letter-spacing
      letter-spacing: 0.05em;
      text-indent: 0.05em;
    }
    .logo-main {
      height: auto;
      width: 200px;
      color: #fc9779;
      line-height: 52px;
      font-family: "Oswald", sans-serif;
      font-size: 52px;
      font-weight: 400;
      // recenter after change the letter-spacing
      text-align: center;
      letter-spacing: 0.08em;
      text-indent: 0.08em;
      .bg-stripe {
        margin-top: -23px;
        height: 20px;
        background: linear-gradient(
          45deg,
          #000000 25%,
          #ffffff 0,
          #ffffff 50%,
          #000000 0,
          #000000 75%,
          #ffffff 0
        );
        background-size: 3px 3px;
      }
    }
    .logo-sub {
      padding-top: 16px;
      line-height: 11px;
      font-family: "Lato", sans-serif;
      font-size: 11px;
      font-weight: 300;
      // recenter after change the letter-spacing
      letter-spacing: 0.18em;
      text-indent: 0.18em;
    }
  }
  .top-right {
    grid-column: 4;
    grid-row: 2;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    .user-status {
      padding-bottom: 10px;
      button {
        outline: none;
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        justify-content: space-between;
        align-items: center;
        background-color: transparent;
        border: none;
        padding: 6px 10px 6px 0px;
        .icon {
          width: 26px;
          height: 26px;
          padding: 0px 14px;
        }
        color: #fc9779;
        font-size: 14px;
        font-family: "Nunito Sans", sans-serif;
        cursor: pointer;
        &:hover {
          filter: brightness(50%);
          transition: 0.4s;
        }
      }
    }
    .search {
      input {
        background-color: transparent;
        border-radius: 0px;
        border-color: #fc9779;
        border-width: 0.1px;
      }
      ::placeholder {
        color: white;
        font-family: "Lato";
      }
      &:hover {
        border-color: white;
        transition: 0.4s;
      }
    }
  }
  .login-popup {
    animation: none;
    background-color: black;
  }
}
</style>

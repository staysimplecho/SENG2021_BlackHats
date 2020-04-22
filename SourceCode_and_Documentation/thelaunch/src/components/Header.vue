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
      <el-card style="background-color:black;border:none;margin-top:100px">
        <h2
          style="font-family:anton;font-size:50px;text-align:center;color:white;"
        >
          Sign Up
        </h2>
        <p style="text-align:center">
          <span style="color:white;font-size:20px;">Already a member? </span
          ><a><span style="color:#fc9779;font-size:20px;">Log In</span></a>
        </p>
        <div style="height:40px;"></div>
        <div v-if="!signUp">
          <el-button
            style="background-color:rgb(71,89,149);color:white;border:none;width:280px;height:60px;margin-left:40%"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 266.89 266.89"
              style="width:40px;height:40px;display:flex;flex-direction:row;margin-top:-10px"
            >
              <g>
                <path
                  style="fill:#fff;"
                  d="M252.16,0H14.73A14.73,14.73,0,0,0,0,14.73V252.16a14.73,14.73,0,0,0,14.73,14.73H142.55V163.57H107.77V123.29h34.82V93.58c0-34.47,21.06-53.24,51.81-53.24a285.41,285.41,0,0,1,31.08,1.59v36H204.15c-16.76,0-20,8-20,19.61v25.72H224l-5.16,40.28H184.15V266.89h68a14.73,14.73,0,0,0,14.73-14.73V14.73A14.73,14.73,0,0,0,252.16,0Z"
                ></path>
              </g>
            </svg>
            <span
              style="margin-top:-30px;margin-left:50px;font-size:20px;display:flex;flex-direction:row;"
              >Sign up with Facebook</span
            >
          </el-button>
          <div style="height:20px;"></div>
          <el-button
            style="background-color:rgb(92,132,241);color:white;border:none;width:280px;height:60px;margin-left:40%"
          >
            <img
              src="../assets/google.png"
              style="width:40px;height:40px;float:left;display:flex;flex-direction:row;"
            />
            <span
              style="margin-top:10px;margin-left:50px;font-size:20px;display:flex;flex-direction:row;"
              >Sign up with Google</span
            >
          </el-button>
          <div style="display:flex;margin-left:39%;margin-top:20px">
            <div
              style="border:0.5px solid white;width:150px;height:0;flex-direction:row"
            ></div>
            <span style="color:white;flex-direction:row;margin-top:-10px;">
              or
            </span>
            <div
              style="border:0.5px solid white;width:150px;height:0;flex-direction:row"
            ></div>
          </div>
          <div style="height:20px;"></div>
          <el-button
            @click="tosignUp"
            style="background-color:black;width:280px;height:60px;position:absolute;margin-left:39%"
          >
            <span style="color:white;font-size:20px">Sign up with email</span>
          </el-button>
        </div>
        <div v-else style="margin-left:39%">
          <el-form
            class="signup-form"
            :model="model"
            :rules="rules"
            ref="form"
            @submit.native.prevent="signup"
          >
            <el-form-item prop="Email">
              <el-input v-model="model.email" placeholder="Email"></el-input>
            </el-form-item>
            <el-form-item prop="password">
              <el-input
                v-model="model.password"
                placeholder="Password"
                type="password"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-button
                class="signup-button"
                type="primary"
                native-type="submit"
                block
                >Sign Up</el-button
              >
            </el-form-item>
          </el-form>
        </div>
      </el-card>
      <!--<div>
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
      </div>-->
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
      signUp: false,
      loading:false,
      validCredentials: {
        email: "mc.huang.jl@gmail.com",
        password: "lightscope"
      },
      model: {
        email: null,
        password: null,
      },
      rules: {
        email: [
          {
            required: true,
            message: "Email is required",
            trigger: "blur",
          },
          {
            message: "Email length should be in example@example.com",
            trigger: "blur",
          },
        ],
        password: [
          { required: true, message: "Password is required", trigger: "blur" },
          {
            min: 5,
            message: "Password length should be at least 5 characters",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    backHome() {
      this.$router.push({
        name: "Home",
      });
    },
    tosignUp() {
      this.signUp = true;
    },
    simulateLogin() {
      return new Promise(resolve => {
        setTimeout(resolve, 800);
      });
    },
    async signup() {
      let valid = await this.$refs.form.validate();
      if (!valid) {
        return;
      }
      this.loading = true;
      await this.simulateLogin();
      this.loading = false;
      if (
        this.model.email === this.validCredentials.email &&
        this.model.password === this.validCredentials.password
      ) {
        this.$message.success("Login successfull");
      } else {
        this.$message.error("Email or password is invalid");
      }
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
.signup-form {
  width: 290px;
}
.signup-button {
  width: 100%;
  margin-top: 40px;
}
</style>

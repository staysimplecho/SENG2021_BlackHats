<template>
  <div id="account-wrap">
    <div class="account-title">
      <div class="account-title-main">My Account</div>
      <div class="account-title-sub">
        View and edit your personal info below.
      </div>
    </div>
    <div class="account-content">
      <div class="edit-item">
        <div class="property">Login Email:</div>
        <div class="field">
          oh0917ce@gmail.com
          <el-tooltip placement="top" effect="light">
            <div slot="content">
              Your login email<br />
              can’t be changed.
            </div>
            <i class="el-icon-info"></i>
          </el-tooltip>
        </div>
      </div>
      <div class="edit-item_fn">
        <div class="property">First Name</div>
        <div class="field">
          <input
            class="input-slot"
            form="submit"
            placeholder="e.g., Kate"
            type="text"
          />
        </div>
      </div>
      <div class="edit-item_ln">
        <div class="property">Last Name</div>
        <div class="field">
          <input
            class="input-slot"
            form="submit"
            placeholder="e.g., Sams"
            type="text"
          />
        </div>
      </div>
      <div class="edit-item_ce">
        <div class="property">Contact Email</div>
        <div class="field">
          <input
            class="input-slot"
            form="submit"
            placeholder="oh0917ce@gmail.com"
            type="text"
          />
        </div>
      </div>
      <div class="edit-item_ph">
        <div class="property">Phone</div>
        <div class="field">
          <input
            class="input-slot"
            form="submit"
            placeholder="e.g., +61 041-152-2346"
            type="text"
          />
        </div>
      </div>
      <div class="edit-item_btn">
        <input class="input-btn" type="submit" value="Update Info" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      submit: {
        fn: "",
        ln: "",
        ce: "",
        ph: "",
      },
    };
  },
};
</script>

<style lang="scss" scoped>
#account-wrap {
  width: 100%;
  padding: 0 30px;
  color: white;
  font-family: "Avenir-LT-W01_35-Light1475496";
  .account-title {
    padding: 20px 0px;
    border-bottom: solid rgba(128, 128, 128, 0.5) 1px;
    &-main {
      margin: 10px;
      font-size: 26px;
    }
    &-sub {
      font-weight: bold;
      font-size: 16px;
      margin: 10px;
    }
  }

  .account-content {
    margin-top: 30px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 90px 1fr 1fr;
    grid-template-areas:
      "ensure btn"
      "fn ln"
      "ce ph";
    .property,
    .field {
      margin: 10px;
      font-weight: bold;
      font-size: 15px;
      i {
        margin: 0px 10px;
      }
      .input-slot {
        outline: none;
        border: solid rgba(128, 128, 128, 0.5) 1px;
        width: 288px;
        height: 42px;
        padding: 0 10px;
        &::placeholder {
          text-indent: 1em;
        }
      }
    }
    .edit-item {
      grid-area: ensure;
      //   margin: 30px 0px;
    }
    .edit-item_fn {
      grid-area: fn;
      margin: 20px 0px;
    }
    .edit-item_ln {
      grid-area: ln;
      margin: 20px 0px;
    }
    .edit-item_ce {
      grid-area: ce;
      margin: 20px 0px;
      .field.input-slot::placeholder {
        color: white;
        opacity: 1;
      }
    }
    .edit-item_ph {
      grid-area: ph;
      margin: 20px 0px;
    }
    .edit-item_btn {
      grid-area: btn;
      align-self: center;
      margin: 20px 10px;
      .input-btn {
        color: black;
        border: none;
        outline: none;
        background-color: #fc9779;
        width: 200px;
        height: 40px;
        &:hover,
        &:active {
          background-color: #fc97797e;
          transition: 0.4s ease-in-out;
        }
      }
    }
  }
}
</style>

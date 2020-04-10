<template>
  <div id="header-wrap">
    <nav class="navigation">
      <router-link to="/"><p>HOME</p></router-link>
      <router-link to="/events"><p>SHOWS</p></router-link>
      <router-link to="/artists"><p>ARTISTS</p></router-link>
      <router-link to="/news"><p>NEWS</p></router-link>
      <router-link to="/contact"><p>CONTACT</p></router-link>
    </nav>
    <div>
      <span>The</span>
      <span>LAUNCH</span>
    </div>
    <div></div>
  </div>
</template>

<style lang="scss">
#header-wrap {
  display: flex;
  width: 100%;
  .navigation {
    display: flex;
    p {
      color: white;
      height: 50px;
      line-height: 50px;
      text-align: center;
      padding: 0 15px;
      font-size: 16px;
      font-weight: normal;
      font-family: "Pathway Gothic One";
    }
  }
}
</style>

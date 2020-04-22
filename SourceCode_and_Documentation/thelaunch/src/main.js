import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import * as VueGoogleMaps from "vue2-google-maps";
import { VueMasonryPlugin } from "vue-masonry";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
// import '@fortawesome/fontawesome-free/css/all.css' // Ensure you are using css-loader
import '@mdi/font/css/materialdesignicons.css';
import VueSimpleAlert from "vue-simple-alert";
import SimpleVueValidation from "simple-vue-validator";

Vue.config.producWtionTip = false;
Vue.use(ElementUI);
Vue.use(Vuetify);
export default new Vuetify({
  icons: {
    iconfont: "mdi", // default - only for display purposes
  },
});
Vue.use(VueMasonryPlugin);
Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyBNmajm_tGfxednNNM5uzONqYoxyiLagTk",
    libraries: "places",
  },
  installComponents: true,
});
Vue.use(VueSimpleAlert);
Vue.use(SimpleVueValidation);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");

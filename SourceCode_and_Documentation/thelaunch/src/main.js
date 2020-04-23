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
import '@mdi/font/css/materialdesignicons.css';
import VueSimpleAlert from "vue-simple-alert";
import SimpleVueValidation from "simple-vue-validator";
import fullCalendar from 'vue-fullcalendar'

Vue.component('full-calendar', fullCalendar)

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

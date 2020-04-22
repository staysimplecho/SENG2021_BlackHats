import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Events from "../views/Events.vue";
import Artists from "../views/Artists.vue";
import News from "../views/News.vue";
import Contact from "../views/Contact.vue";
import EventInfo from "../views/EventInfo.vue";
import ArtistInfo from "../views/ArtistInfo.vue";
import Profile from "../views/Profile.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/events",
    name: "Shows",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Events,
    // component: () =>
    //   import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/events/:id",
    name: "EventPage",
    component: EventInfo,
  },
  {
    path: "/artists",
    name: "Artists",
    component: Artists,
  },
  {
    path: "/artists/:id",
    name: "ArtistPage",
    component: ArtistInfo,
  },
  {
    path: "/news",
    name: "News",
    component: News,
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
  },
  // :id
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
    children:[]
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

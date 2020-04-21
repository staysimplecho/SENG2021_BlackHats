var artists = require("./src/assets/artists/data.json"); //本地json文件数据

module.exports = {
  productionSourceMap: false,

  devServer: {
    before(app) {
      app.get("/api/artists", (req, res) => {
        res.json({
          errno: 0, // 这里是你的json内容
          data: artists,
        });
      });
    },
    open: process.platform === "darwin",
    host: "0.0.0.0",
    port: 8080,
    https: false,
    hotOnly: false,
    proxy: null, // 设置代理
  },

  css: {
    loaderOptions: {
      sass: {
        prependData: `
          @import "@/assets/css/global.scss";
          @import "@/assets/css/fonts.scss";
        `,
      },
    },
  },
};

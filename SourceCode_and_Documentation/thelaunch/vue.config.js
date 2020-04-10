module.exports = {
  productionSourceMap: false,

  devServer: {
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
        `,
      },
    },
  },
};

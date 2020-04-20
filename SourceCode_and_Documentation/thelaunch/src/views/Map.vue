<template>
  <div>
    <div ref="map" style="width:482px;height:308px;"></div>
  </div>
</template>

<script>
export default {
  name: "Map",
  data() {
    return {
      platform: {},
      map: {},
    };
  },
  props: {
    apiKey: String,
    latitude: String,
    longitude: String,
    zoom: String,
  },
  created() {
      this.platform = new Map.service.Platform({
          "apikey": this.apiKey
      });
  },
  mounted() {
      this.map = new Map.map(
          this.$refs.map,
          this.platform.createDefaultLayers().vector.normal.map,
          {
              zoom: this.zoom,
              center: { lat: this.latitude, lng: this.longitude}
          }
      );
  },
  methods: {
      dropMarker(position) {
          let marker = new Map.map.Marker({ lat: position.Latitude, lng: position.Longitude });
            this.map.addObject(marker);
      }
  }
};
</script>

<style scoped lang="scss"></style>

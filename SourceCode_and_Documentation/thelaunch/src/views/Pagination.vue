<template>
  <div>
    <div v-if="totalPages() > 0" class="pagination-wrapper">
      <div style="display:inline-block;">
        <span
          v-if="showPreviousLink()"
          class="pagination-btn"
          @click="updatePage(currentPage - 1)"
          >&laquo; Previous</span
        >
      </div>
      <div style="float:right; display:inline-block;">
        <span
          v-if="showNextLink()"
          class="pagination-btn"
          v-on:click="updatePage(currentPage + 1)"
          >Next &raquo;</span
        >
      </div>
      <div style="margin:0 auto;display:table;">
        {{ currentPage }} of {{ totalPages() }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Pagination",
  props: ["newsPages", "currentPage", "pageSize"],
  methods: {
    updatePage(pageNumber) {
      this.$emit("page:update", pageNumber);
    },
    totalPages() {
      return Math.ceil(this.newsPages.length / this.pageSize);
    },
    showPreviousLink() {
      return this.currentPage == 1 ? false : true;
    },
    showNextLink() {
      return this.currentPage == this.totalPages() ? false : true;
    },
  },
  data() {
    return {};
  },
};
</script>

<style scoped lang="scss">
.pagination-btn {
  cursor: pointer;
}
</style>

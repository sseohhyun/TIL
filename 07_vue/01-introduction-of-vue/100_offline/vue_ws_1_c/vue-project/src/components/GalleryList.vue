<template>
  <main class="container py-3">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      <div class="col" v-for="(item, index) in numberOfItems" :key="index">
        <GalleryListItem />
      </div>
    </div>
  </main>
</template>

<script setup>
import GalleryListItem from '@/components/GalleryListItem.vue'

const numberOfItems = 4
</script>

<style scoped>
</style>

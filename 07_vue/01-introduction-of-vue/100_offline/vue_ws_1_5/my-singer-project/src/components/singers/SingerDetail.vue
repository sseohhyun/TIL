<template>
  <card class="singer-detail">
    <h1>가수 이름</h1>
    <img src="@/assets/singer.jpg" alt="가수 정보" class="singer-image" />
    <p class="singer-description">
      가수 소개글
    </p>
    <SingerAlbum />
    <SingerAlbum />
  </card>
</template>

<script setup>
import SingerAlbum from './SingerAlbum.vue';
</script>

<style scoped>
.singer-detail {
  border: 1px solid black;
  text-align: center;
  padding: 20px;
}

.singer-image {
  max-width: 200px;
  border-radius: 50%;
  margin-top: 10px;
}

.singer-description {
  margin-top: 20px;
}

</style>

<style>
/* h1 {
  color: green
} */
</style>
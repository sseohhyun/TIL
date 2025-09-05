<template>
  <div class="youtube-card" @click="$emit('play-review', videoId)">
    <img :src="thumbnail" :alt="title" class="youtube-thumb">
    <div class="youtube-info">
      <h4>{{ title }}</h4>
      <p>{{ channelTitle }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  videoId: String,
  title: String,
  channelTitle: String,
  thumbnail: String
})

defineEmits(['play-review'])
</script>

<style scoped>
.youtube-card {
  width: 320px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  margin: 10px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: box-shadow 0.2s;
}
.youtube-card:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.2);
}
.youtube-thumb {
  width: 100%;
  border-radius: 8px 8px 0 0;
}
.youtube-info {
  padding: 10px;
  text-align: center;
}
.youtube-info h4 {
  font-size: 1.1rem;
  margin: 5px 0;
}
.youtube-info p {
  font-size: 0.9rem;
  color: #666;
}
</style>

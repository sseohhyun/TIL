<template>
  <div class="modal-overlay" @click.self="$emit('close-modal')">
    <div class="modal-content">
      <button class="close-button" @click="$emit('close-modal')">&times;</button>
      <h2>리뷰 영상</h2>
      <iframe
        v-if="videoId"
        :src="`https://www.youtube.com/embed/${videoId}`"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
        class="youtube-player"
      ></iframe>
      <div v-else class="no-video">영상을 찾을 수 없습니다.</div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  videoId: {
    type: String,
    required: true
  }
})
defineEmits(['close-modal'])
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}
.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 80%;
  max-width: 800px;
  position: relative;
}
.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  border: none;
  background: none;
  cursor: pointer;
}
.youtube-player {
  width: 100%;
  height: 450px;
  margin-top: 15px;
}
</style>
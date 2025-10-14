<template>
  <div class="modal-overlay" @click.self="$emit('close-modal')">
    <div class="modal-content">
      <button class="close-button" @click="$emit('close-modal')">&times;</button>
      <h2>{{ movieTitle }} 예고편</h2>
      <div v-if="trailerId">
        <iframe
          :src="`https://www.youtube.com/embed/${trailerId}`"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          class="youtube-player"
        ></iframe>
      </div>
      <div v-else class="no-trailer">예고편을 찾을 수 없습니다.</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const props = defineProps({
  movieTitle: {
    type: String,
    required: true
  }
})

defineEmits(['close-modal'])

const trailerId = ref(null)

const YOUTUBE_API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY

onMounted(async () => {
  const query = `${props.movieTitle} 공식 예고편`
  const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${query}&key=${YOUTUBE_API_KEY}&type=video&maxResults=1`
  
  try {
    const response = await axios.get(url)
    const firstResult = response.data.items[0]
    if (firstResult) {
      trailerId.value = firstResult.id.videoId
    }
  } catch (error) {
    console.error('유튜브 예고편을 불러오는 데 실패했습니다:', error)
  }
})
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
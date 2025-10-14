<template>
  <div class="movie-info-container" v-if="movie">
    <div class="movie-header">
      <img :src="posterPath" :alt="movie.title + ' poster'" class="movie-poster">
      <div class="movie-details">
        <h2>{{ movie.title }}</h2>
        <p><strong>개봉일:</strong> {{ movie.release_date }}</p>
        <p><strong>평점:</strong> {{ movie.vote_average.toFixed(1) }}</p>
        <p><strong>장르:</strong> {{ genres }}</p>
        <button @click="$emit('show-trailer')" class="trailer-button">공식 예고편</button>
      </div>
    </div>
    <div class="movie-overview">
      <h3>줄거리</h3>
      <p>{{ movie.overview }}</p>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
})

// 컴포넌트에서 이벤트를 발생시키기 위해 defineEmits 사용
defineEmits(['show-trailer'])

const posterPath = computed(() => {
  if (props.movie.poster_path) {
    return `https://image.tmdb.org/t/p/w500/${props.movie.poster_path}`
  }
  // 포스터가 없을 경우 대체 이미지 사용
  return '[https://via.placeholder.com/500x750?text=No+Poster+Available](https://via.placeholder.com/500x750?text=No+Poster+Available)'
})

const genres = computed(() => {
  return props.movie.genres.map(genre => genre.name).join(', ')
})
</script>

<style scoped>
.movie-info-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.movie-header {
  display: flex;
  gap: 30px;
  align-items: flex-start;
}

.movie-poster {
  width: 300px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.movie-details h2 {
  font-size: 2.5rem;
  margin-top: 0;
  color: #333;
}

.movie-details p {
  font-size: 1.1rem;
  margin: 10px 0;
  color: #666;
}

.movie-overview {
  margin-top: 30px;
  line-height: 1.6;
}

.trailer-button {
  background-color: #ff0000;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.trailer-button:hover {
  background-color: #cc0000;
}
</style>
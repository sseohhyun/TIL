<template>
  <!-- RouterLink를 사용하여 클릭 시 상세 페이지로 이동 -->
  <router-link :to="{ name: 'movie-detail', params: { movieId: movie.id } }">
    <div class="movie-card">
      <img :src="posterPath" :alt="movie.title + ' poster'" class="poster">
      <div class="info">
        <h3>{{ movie.title }}</h3>
        <p>{{ movie.overview }}</p>
      </div>
    </div>
  </router-link>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
})

// 포스터 이미지 경로를 생성하는 계산된 속성
const posterPath = computed(() => {
  return `https://image.tmdb.org/t/p/w500/${props.movie.poster_path}`
})
</script>

<style scoped>
.movie-card {
  width: 250px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin: 15px;
  cursor: pointer;
  transition: transform 0.2s;
}

.movie-card:hover {
  transform: scale(1.05);
}

.poster {
  width: 100%;
  height: auto;
}

.info {
  padding: 15px;
}

.info h3 {
  font-size: 1.2rem;
  margin-bottom: 5px;
}

.info p {
  font-size: 0.9rem;
  color: #555;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
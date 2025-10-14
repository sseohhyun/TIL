<template>
  <div class="movie-list-container">
    <h1>최고 평점 영화 목록</h1>
    <div v-if="loading" class="loading">영화 정보를 불러오는 중...</div>
    <div v-else class="movie-grid">
      <!-- v-for를 사용하여 영화 목록을 순회하며 MovieCard 컴포넌트를 렌더링 -->
      <MovieCard
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import MovieCard from '@/components/MovieCard.vue'
import axios from 'axios'

const movies = ref([])
const loading = ref(true)

// .env 파일에서 TMDB API 키를 가져옴
const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY

onMounted(async () => {
  const url = `https://api.themoviedb.org/3/movie/top_rated?api_key=${TMDB_API_KEY}&language=ko-KR&page=1`
  try {
    const response = await axios.get(url)
    movies.value = response.data.results
  } catch (error) {
    console.error('영화 목록을 불러오는 데 실패했습니다:', error)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.movie-list-container {
  padding: 20px;
}

.movie-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  justify-items: center;
}
</style>
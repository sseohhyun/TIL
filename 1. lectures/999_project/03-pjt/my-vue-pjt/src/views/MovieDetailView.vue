<template>
  <div class="movie-detail-container">
    <div v-if="loading" class="loading">영화 상세 정보를 불러오는 중...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <!-- 영화 상세 정보 컴포넌트 -->
      <MovieDetailInfo :movie="movie" @show-trailer="showTrailerModal = true" />
      
      <!-- 예고편 모달 -->
      <YoutubeTrailerModal
        v-if="showTrailerModal"
        :movie-title="movie.title"
        @close-modal="showTrailerModal = false"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import MovieDetailInfo from '@/components/MovieDetailInfo.vue'
import YoutubeTrailerModal from '@/components/YoutubeTrailerModal.vue'

const route = useRoute()
const movie = ref(null)
const loading = ref(true)
const error = ref(null)
const showTrailerModal = ref(false)

const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY

onMounted(async () => {
  const movieId = route.params.movieId
  if (!movieId) {
    error.value = '영화 ID가 없습니다.'
    loading.value = false
    return
  }

  const url = `https://api.themoviedb.org/3/movie/${movieId}?api_key=${TMDB_API_KEY}&language=ko-KR`
  try {
    const response = await axios.get(url)
    movie.value = response.data
  } catch (err) {
    console.error('영화 상세 정보를 불러오는 데 실패했습니다:', err)
    error.value = '영화 정보를 찾을 수 없습니다.'
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.movie-detail-container {
  padding: 20px;
}
</style>
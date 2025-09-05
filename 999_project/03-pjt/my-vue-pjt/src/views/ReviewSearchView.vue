<template>
  <div class="review-search-container">
    <h1>영화 리뷰 검색</h1>
    <div class="search-box">
      <input
        type="text"
        v-model="searchQuery"
        @keyup.enter="searchReviews"
        placeholder="영화 제목을 입력하세요..."
      />
      <button @click="searchReviews">검색</button>
    </div>
    
    <div v-if="loading" class="loading">리뷰 영상을 검색하는 중...</div>
    <div v-else class="youtube-grid">
      <!-- v-for를 사용하여 검색 결과를 순회하며 YoutubeCard 컴포넌트를 렌더링 -->
      <YoutubeCard
    v-for="video in videos"
    :key="video.id.videoId"
    :videoId="video.id.videoId"
    :title="video.snippet.title"
    :channelTitle="video.snippet.channelTitle"
    :thumbnail="video.snippet.thumbnails.medium.url"
    @play-review="showReviewModal"
      />
    </div>
    
    <!-- 리뷰 모달 -->
    <YoutubeReviewModal
      v-if="showModal"
      :videoId="selectedVideoId"
      @close-modal="closeReviewModal"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import YoutubeCard from '@/components/YoutubeCard.vue'
import YoutubeReviewModal from '@/components/YoutubeReviewModal.vue'

const searchQuery = ref('')
const videos = ref([])
const loading = ref(false)
const showModal = ref(false)
const selectedVideoId = ref(null)

const YOUTUBE_API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY

const searchReviews = async () => {
  if (!searchQuery.value) return

  loading.value = true
  const query = `${searchQuery.value} 영화 리뷰`
  const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${query}&key=${YOUTUBE_API_KEY}&type=video&maxResults=10`
  
  try {
    const response = await axios.get(url)
    videos.value = response.data.items
  } catch (error) {
    console.error('유튜브 리뷰 검색에 실패했습니다:', error)
  } finally {
    loading.value = false
  }
}

const showReviewModal = (videoId) => {
  selectedVideoId.value = videoId
  showModal.value = true
}

const closeReviewModal = () => {
  showModal.value = false
  selectedVideoId.value = null
}
</script>

<style scoped>
.review-search-container {
  padding: 20px;
}

.search-box {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.search-box input {
  width: 400px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.search-box button {
  padding: 10px 20px;
  margin-left: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.youtube-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}
</style>

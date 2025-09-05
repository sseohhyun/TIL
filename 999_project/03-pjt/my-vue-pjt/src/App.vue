<template>
  <div id="app" class="bg-gray-100 min-h-screen font-sans antialiased">
    <!-- 헤더 영역 -->
    <header class="bg-gradient-to-r from-blue-500 to-purple-600 text-white p-4 shadow-lg">
      <nav class="container mx-auto flex justify-between items-center">
        <div class="space-x-4">
          <router-link to="/" class="text-white hover:text-gray-200 transition duration-300 ease-in-out">Home</router-link>
          <router-link to="/movies" class="text-white hover:text-gray-200 transition duration-300 ease-in-out">Movies</router-link>
          <router-link to="/review-search" class="text-white hover:text-gray-200 transition duration-300 ease-in-out">Review Search</router-link>
        </div>
      </nav>
    </header>
    
    <!-- 메인 콘텐츠 영역 -->
    <main class="container mx-auto mt-8 p-4 bg-white rounded-lg shadow-lg">
      <router-view />
    </main>
  </div>
</template>

<script setup>

</script>

<style scoped>
.space-x-4 > * {
  margin-right: 24px;
}
.space-x-4 > *:last-child {
  margin-right: 0;
}
</style>
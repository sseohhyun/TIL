<template>
  <div class="album">
    <div class="album-header">
      <p class="album-title">앨범 제목</p>
    </div>
    <ul class="song-list">
      <li class="song">노래 목록 1</li>
      <li class="song">노래 목록 2</li>
      <li class="song">노래 목록 3</li>
    </ul>
  </div>
</template>

<style scoped>
.album {
  display: inline-block;
  text-align: center;
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f5f5f5;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.album-header {
  position: relative;
}

.album-cover {
  max-width: 150px;
  border-radius: 8px;
}

.album-title {
  margin-top: 5px;
  font-size: 18px;
  font-weight: bold;
}

.song-list {
  list-style: none;
  padding: 0;
  margin-top: 20px;
}

.song {
  margin: 8px 0;
  font-size: 16px;
  color: #ff6600;
  transition: color 0.2s ease-in-out;
}
</style>

<template>
  <h1>글꼴 테스트기</h1>
  <ul>
      <li v-for="font in fonts" :key="font.style">
        <label>{{ font.style }} 테스트</label>
        <input v-model="font.text">
        <div v-if="font.text" :style="{ fontFamily: font.style }">{{ font.text }}</div>
      </li>
  </ul>
</template>

<script setup>
  import { ref } from 'vue'

  const fonts = ref([
    { style: '바탕', text: '' },
    { style: '휴먼엽서체', text: '' },
    { style: '궁서체', text: '' },
  ])
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  background-color: #f5f5f5;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input {
  width: calc(100% - 12px);
  margin-bottom: 5px;
  padding: 5px;
}
</style>
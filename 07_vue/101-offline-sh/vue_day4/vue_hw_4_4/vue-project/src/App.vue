<template>
  <div>
    <nav>
      <router-link to="/">main</router-link>
    </nav>
    <h1>pinia + router 연습하기</h1>
    <router-view />
  </div>
</template>

<script setup>
// ...existing code...
</script>

<style scoped>
nav {
  margin-bottom: 16px;
}
</style>
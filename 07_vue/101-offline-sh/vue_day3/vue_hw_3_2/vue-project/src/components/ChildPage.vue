<template>
  <article>
    <h3>자식 페이지입니다.</h3>
    <p>이름: {{ myName }}</p>
    <p>나이: {{ myAge }}</p>
  </article>
</template>

<script setup>
defineProps({
  myName: String,
  myAge: Number
})
</script>

<style scoped>
article {
  border: 1px solid gray;
  padding: 15px;
  margin: 15px;
}
</style>
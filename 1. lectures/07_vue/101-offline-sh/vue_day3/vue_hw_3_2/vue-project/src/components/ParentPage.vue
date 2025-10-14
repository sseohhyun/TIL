<template>
  <section>
    <h1>부모 페이지입니다.</h1>
    <ChildPage 
      v-for="info in children"
      :my-name="info.name"
      :my-age="info.age"
    />
  </section>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue';

const children = ref([
  {name: '김하나', age: 30},
  {name: '김두리', age: 20},
  {name: '김서이', age: 10},
])

</script>

<style scoped>
section {
  border: 1px solid gray;
  padding: 15px;
  margin: 15px;
}
</style>
<template>
  <section>
    <h1>부모 페이지입니다.</h1>
    <ChildPage 
      v-for="info in children"
      :my-name="info.name"
      :my-age="info.age"
      :my-balance="info.balance"
      @give-me-allowance="updateBalance"
    />
  </section>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from './ChildPage.vue';

const children = ref([
  {name: '김하나', age: 30, balance: 100000},
  {name: '김두리', age: 20, balance: 10000},
  {name: '김서이', age: 10, balance: 1000},
])
const updateBalance = function(name) {
  children.value.forEach(info => {
    if (info.name === name) {
      info.balance += 1000
    }
  })
}
</script>

<style scoped>
section {
  border: 1px solid gray;
  padding: 15px;
  margin: 15px;
}
</style>
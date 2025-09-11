<template>
  <div class = "child">
    <h3>자식 페이지</h3>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  child: Object
})
</script>

<style scoped>
.child {
  background-color: white;
  border: solid rgb(226, 226, 226) 3px;
  padding: 10px;
  margin-top: 10px;
}
</style>
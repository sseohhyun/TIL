<template>
  <div class="parent">
    <h3>부모 컴포넌트</h3>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage 
      v-for="child in family.children"
      :key="child.name"
      :child="child"
    />
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
import ChildPage from './ChildPage.vue';

defineProps({
  family: Object
})
</script>

<style scoped>
.parent {
  background-color: rgb(240, 240, 240);
  border: 3px solid rgb(216, 216, 216);
  padding: 15px;
  margin-bottom: 20px;
}
</style>
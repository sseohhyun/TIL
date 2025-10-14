<template>
  <div>
    <h1>pinia 연습하기</h1>
    <ParentPage 
      v-for="family in store.familyInfo" 
      :key="family.familyName" 
      :family="family" 
    />
  </div>
</template>

<script setup>
import ParentPage from './ParentPage.vue';
import { useFamilyStore } from '@/stores/family'

const store = useFamilyStore()
</script>

<style scoped>
h1 {
  margin-bottom: 20px;
}
</style>
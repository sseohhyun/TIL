<template>
  <div>
    <div>이름: {{ name }}</div>
    <div>잔고: {{ balance }}</div>
    <button @click="goUpdate">updateBalance</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const props = defineProps(['name', 'balance'])
const router = useRouter()
function goUpdate() {
  router.push({ name: 'update', params: { name: props.name } })
}
</script>

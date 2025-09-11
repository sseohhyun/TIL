<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <div v-if="target">
      <div>이름: {{ target.name }}</div>
      <div>잔고: {{ target.balance }}</div>
      <button @click="plusBalance">+</button>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useBalanceStore } from '../stores/balance'
import { computed } from 'vue'

const route = useRoute()
const balanceStore = useBalanceStore()
const target = computed(() => balanceStore.getByName(route.params.name))

function plusBalance() {
  if (target.value) {
    target.value.balance += 1000
  }
}
</script>

<style>
</style>
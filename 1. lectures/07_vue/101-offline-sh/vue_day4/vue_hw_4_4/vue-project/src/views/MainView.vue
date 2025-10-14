<template>
  <div>
    <h2>메인 페이지</h2>
    <MainPage
      v-for="item in balances"
      :key="item.name"
      :name="item.name"
      :balance="item.balance"
    />
  </div>
</template>

<script setup>
import { useBalanceStore } from '../stores/balance'
import { storeToRefs } from 'pinia'
import MainPage from '../components/MainPage.vue'

const balanceStore = useBalanceStore()
const { balances } = storeToRefs(balanceStore)
</script>

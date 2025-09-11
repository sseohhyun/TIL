<template>
  <section>
    <h1>Parent</h1>
    <ParentChild 
      my-msg="message"
      :my-balance="balance"
    />
    <ParentItem 
      v-for="info in children" 
      :key="info.name"
      :my-info="info"
      @balance-update="onBalanceUpdate"
    />
  </section>
</template>

<script setup>
import ParentChild from './ParentChild.vue';
import ParentItem from './ParentItem.vue';
import { ref } from 'vue'

const balance = ref(10000)
const children = ref([
  {name: "Alice", balance: 100},
  {name: "Bella", balance: 1000},
  {name: "Chalie", balance: 10000},
])
const onBalanceUpdate = function(name) {
  // console.log('용돈 올려달라고? who are you~?')
  // console.log(name)
  children.value.forEach(info => {
    if (info.name === name) {
      if (info.balance <= 50000) {
        info.balance += 1000
      } else {
        alert("이미 많아")
      }
    }
  })
}

</script>

<style scoped>

</style>
<template>
  <article>
    <h3>자식 페이지입니다.</h3>
    <p>이름: {{ myName }}</p>
    <p>나이: {{ myAge }}</p>
    <p>용돈: {{ myBalance }}</p>
    <button @click="giveMeAllowance">용돈 주세요.</button>
  </article>
</template>

<script setup>
const props = defineProps({
  myName: String,
  myAge: Number,
  myBalance: Number
})
const emit = defineEmits(['giveMeAllowance'])

const giveMeAllowance = function () {
  emit('giveMeAllowance', props.myName)
}
</script>

<style scoped>
article {
  border: 1px solid gray;
  padding: 15px;
  margin: 15px;
}
</style>

updateBalance
giveMeAllowance
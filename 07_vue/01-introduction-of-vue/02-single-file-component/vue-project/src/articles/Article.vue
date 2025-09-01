<template>
  <div>
    {{ message }}
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  const message = ref('hello, articles')
</script>
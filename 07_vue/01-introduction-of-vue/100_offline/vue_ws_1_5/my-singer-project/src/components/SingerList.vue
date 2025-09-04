<template>
  <div class="singer-list">
    <h1>가수 목록</h1>
    <ul class="singer-items">
      <SingerDetail 
        v-for="singer in singers"
        :key="singer.name"
      />
    </ul>
  </div>
</template>

<script setup>
  import SingerDetail from './singers/SingerDetail.vue';
  const singers = [
    {
      name: 'adele'
    },
    {
      name: 'maroont 5'
    },
    {
      name: 'Dua Lipa'
    },
    ]
</script>

<style scoped>
card {
  display: inline-block;
  width: 40%;
  margin: 20px;
}

h1 {
  color: orangered
}

.singer-list {
  text-align: center;
}

.singer-items {
  list-style: none;
  padding: 0;
}
</style>
<template>
  <div>
    <header class="sticky-top p-3 d-flex justify-content-center align-items-center bg-success-subtle">
      <h1 class="display-1">My Gallery</h1>
    </header>

    <main class="container py-3">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div class="col" v-for="_ in numberOfItems">
          <div class="card">
            <img src="@/assets/sample.png" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
const numberOfItems = 4
</script>

<style scoped>

</style>

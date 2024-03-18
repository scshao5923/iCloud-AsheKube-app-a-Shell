<template>
    <div>
      <h2>{{ foodName }}</h2>
      <p>{{ foodDesc }}</p>
      <img src="/favicon.ico" v-show="isFavorite"/>
    </div>
  </template>
  
  <script>
    export default {
      props: [
        'foodName',
        'foodDesc',
        'isFavorite'
      ]
    }
  </script>
  
  <style></style>
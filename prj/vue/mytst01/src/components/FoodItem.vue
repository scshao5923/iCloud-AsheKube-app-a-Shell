<template>
    <div>
      <h2>{{ foodName }}</h2>
      <p>{{ foodDesc }}</p>
      <img src="/favicon.ico" v-show="isFavorite"/>
    </div>
  </template>
  
  <script>
    export default {
      data(){
        return {
          eric:'eric'
        }
        
      },
      // props: [
      //   'foodName',
      //   'foodDesc',
      //   'isFavorite'
      // ]
      props:{
        foodName:{
          type: String,
          required: true
        },
        foodDesc: String,
        isFavorite: Boolean
      }
    }
  </script>
  
  <style></style>
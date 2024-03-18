<template>
  <h1>Food</h1>
  <food-item foodName="Apples"/>
  <food-item foodName="Pizza"/>
  <food-item foodName="Rice"/>
</template>

<script></script>

<style>
#app>div {
  border: dashed black 1px;
  display: inline-block;
  margin: 10px;
  padding: 10px;
  background-color: lightgreen;
}

#app>div:hover {
  cursor: pointer;
}
</style>
<template>
  <div>
    <h2>{{ foodName }}</h2>
    <p>{{ foodDesc }}</p>
    <img src="/favicon.ico" v-show="isFavorite" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      eric: 'eric'
    }

  },
  // props: [
  //   'foodName',
  //   'foodDesc',
  //   'isFavorite'
  // ]
  props: {
    foodName: {
      type: String,
      required: true
    },
    foodDesc: {
      type: String,
      required: false,
      default: 'This is the default description.',
      validator: value => ( 20<value.length && value.length<50 ) ? true: false
    },
    isFavorite: {
      type: Boolean,
      required: false,
      default: false
    }
  }
}
</script>

<style></style>
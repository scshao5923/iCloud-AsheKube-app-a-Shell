<template>
  <div>
    <h2>{{ foodName }}</h2>
    <p>{{ foodDesc }}</p>
    <img src="/favicon.ico" v-show="foodIsFavorite" />
    <button v-on:click="toggleFavorite">Like</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      eric: 'eric',
      foodIsFavorite: this.isFavorite
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
      validator: value => (20 < value.length && value.length < 50) ? true : false
    },
    isFavorite: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  methods: {
    toggleFavorite() {
      this.foodIsFavorite = !this.foodIsFavorite;
    }
  }
}
</script>

<style></style>
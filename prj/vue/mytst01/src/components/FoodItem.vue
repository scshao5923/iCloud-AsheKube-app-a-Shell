<template>
    <div v-on:click="countClicks">
        <h2>{{ name }}</h2>
        <p>{{ message }}</p>
        <p>foodName:{{ foodName }}</p>
        <p id="red">You have clicked me {{ clicks }} times.</p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            name: 'Apples',
            message: 'I like apples',
            clicks: 0
        }
    },
    methods: {
        countClicks() {
            this.clicks++
        }
    },
    props:[
        "foodName"
    ]
};
</script>

<style>
#red {
    font-weight: bold;
    color: rgb(144, 12, 12);
}
</style>
<script setup>
const props = defineProps({
  msg: String,
  name: String
})
</script>

<template>
  <br />
  <button @click="$emit('goBack')">Back</button>
  <h3>{{ name }}</h3>
  <div v-html="msg"></div>
</template>
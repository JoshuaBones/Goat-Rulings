<script setup>
const props = defineProps({
  msg: String,
  name: String
})
defineEmits(['goBack', 'findMentions'])
</script>

<template>
  <br />
  <div class="center">
    <button @click="$emit('goBack')">Back</button>
    <button @click="$emit('findMentions')" class="l-margin">Mentions</button>
  </div>
  <h3>{{ name }}</h3>
  <div v-html="msg"></div>
</template>
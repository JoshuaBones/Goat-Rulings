<script setup>
import RulingComp from './components/Ruling.vue'

import { ref, watch } from 'vue'
import cardData from './rulings.json'

const cardNames = Object.keys(cardData)

const search = ref("")
const searchResults = ref(null)

const name = ref(null)
const ruling = ref(null)

const namesOrRulings = ref(true)//true to show names false for rulings

async function showRuling(cardName) {
  name.value = cardName
  ruling.value = cardData[cardName]
}

async function fetchMatchingCardNames() {
  const s = search.value.toLowerCase()
  searchResults.value = cardNames.filter(x => x.toLowerCase().includes(s))
}

function toggleNamesOrRulings() {//https://vuejs.org/tutorial/#step-6
  namesOrRulings.value = !namesOrRulings.value
}

//would prefer to use v-model, but that doesn't work on mobile
//so the pre-solution is used here
//https://vuejs.org/tutorial/#step-5
function onInput(e) {
  search.value = e.target.value
}

watch(search, async (newSearch, oldSearch) => {
  fetchMatchingCardNames()
})
</script>

<template>
  <main>
    <div><input :value="search" @input="onInput" placeholder="Search a Card" type="text" @change="fetchMatchingCardNames" /><button @click="fetchMatchingCardNames" type="button">Search</button></div>
    
    <li v-if="namesOrRulings" v-for="(item, index) in searchResults" @click="showRuling(item); toggleNamesOrRulings();">
      {{ item }}
    </li>
    <RulingComp v-else="namesOrRulings" :name="name" :msg="ruling" @goBack="toggleNamesOrRulings()" />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>

<script setup>
import RulingComp from './components/Ruling.vue'

import { onMounted, ref, watch } from 'vue'
import goatData from './rulings.json'
import edisonData from './edison_rulings.json'


const chkFormat = ref("Edison")//search within Goat or Edison data

const goatNames = Object.keys(goatData)
const edisonNames = Object.keys(edisonData)
const cardNames = Object.keys(cards())

const searchInputElement = ref(null)
const chkAutoSearch = ref(null)
const chkSearchType = ref("Card")//search within Name or Ruling

const search = ref("")
const searchResults = ref(null)

const name = ref(null)//current name and ruling being shown in RulingComp
const ruling = ref(null)

const namesOrRulings = ref(true)//true to show names false for rulings

function populateRuling(cardName) {
  name.value = cardName

  if(chkSearchType.value == "Ruling Mentions") {
    //means they're looking for a specific card or text being mentioned, so highlight it
    const re = new RegExp(search.value, "gi")
    ruling.value = cards()[cardName].replaceAll(re, '<mark>$&</mark>')
  } else {
    ruling.value = cards()[cardName]
  }
}

//retrieves card names based on which format is selected
function cardKeys() {
  return chkFormat.value == "Goat" ? goatNames : edisonNames
}

//retrieves card data based on which format is selected
function cards() {
  return chkFormat.value == "Goat" ? goatData : edisonData
}

async function findMentions() {
  document.getElementById("rRuling").checked = true
  chkSearchType.value = "Ruling Mentions"
  toggleNamesOrRulings()
  search.value = name.value
  //fetchMatchingData()
}

async function fetchMatchingData() {
  const s = search.value.toLowerCase()
  
  if(chkSearchType.value == "Card") { //search matching card names
    searchResults.value = cardKeys().filter(x => x.toLowerCase().includes(s))
  } else {                            //retrieve cards based on stored rulings
    searchResults.value = cardKeys().filter((key) => cards()[key].toLowerCase().includes(s))
  }
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

//findMentions() made both watches fire and do the same thing
//https://stackoverflow.com/a/45853349
watch([search, chkSearchType], async () => {
  if(chkAutoSearch.value.checked && search.value != "") {
    fetchMatchingData()
  }
})

//format change - refresh results
watch([chkFormat], async () => {
  //if(search.value != "") {
    fetchMatchingData()
  //}
})

onMounted(() => {
  //https://michaelnthiessen.com/set-focus-on-input-vue#:~:text=Set%20focus%20on%20page%20load
  searchInputElement.value.focus()
})
</script>

<template>
  <main>
    
    <div id="search" class="center">
      <!--div>
        <h2>YGO Rulings</h2>
      </div-->
      <div class="margins">
        <label for="formats">Format: </label>
        <input v-model="chkFormat" type="radio" 
               id="rGoat" 
               value="Goat" 
               class="l-margin">
        <label for="rGoat">Goat</label>
        <input v-model="chkFormat" type="radio"
               id="rEdison" 
               value="Ruling Mentions"
               checked>
        <label for="rEdison">Edison</label>
      </div>
      <div class="margins">
        <input type="checkbox" ref="chkAutoSearch" id="chkAutoSearch" checked>
        <label for="chkAutoSearch">Auto</label>

        <input v-model="chkSearchType" type="radio" 
               id="rCard" 
               value="Card" 
               class="l-margin" 
               checked
        >
        <label for="rCard">Card</label>
        <input v-model="chkSearchType" type="radio"
               id="rRuling" 
               value="Ruling Mentions">
        <label for="rRuling">Ruling Mentions</label>
      </div>
      <input ref="searchInputElement" 
             id="txtInput" 
             :value="search" 
             @input="onInput" 
             placeholder="Search a Card" 
             type="text" 
      />
      <button @click="fetchMatchingData" type="button">Search</button>
    </div>
    
    <div v-if="namesOrRulings" class="text-center-outer">
      <div class="text-center-inner">
        <li v-for="(item, index) in searchResults" 
          @click="populateRuling(item); toggleNamesOrRulings();"
          class="pointer">
          {{ item }}
        </li>
      </div>
    </div>
    <RulingComp v-else 
                :name="name" 
                :msg="ruling" 
                @goBack="toggleNamesOrRulings()"
                @findMentions="findMentions()"
    />
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
    /*padding-right: calc(var(--section-gap) / 2);*/
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

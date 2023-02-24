
<template>
  <div :class="{
    [`${currentPage}-page-body-light`]: !isDarkMode,
    [`${currentPage}-page-body-dark`]: isDarkMode
  }">
    <header>

      
      <div class="wrapper">
        
        <Navbar />

      </div>
    </header>

    <RouterView />
    <Footer />
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import { watchEffect } from 'vue';
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { storeToRefs } from 'pinia';
import Navbar from './components/Navbar/Navbar.vue';
import Footer from './components/Elements/Footer.vue';
import "../public/styles.css"

import { useDarkModeStore } from './stores/darkMode';

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

watchEffect(() => {
  if (darkModeStore.isDarkMode) {
    document.body.classList.remove('body-light')
    document.body.classList.add('body-dark')
  } else if (!darkModeStore.isDarkMode) {
    document.body.classList.remove('body-dark')
    document.body.classList.add('body-light')
  }
}) 

const route = useRoute()
const currentPage = computed(() => {
  return route.name;
});


</script>
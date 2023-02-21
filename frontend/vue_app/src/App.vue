
<template>
  <header>

    
    <div class="wrapper">
      
      <Navbar />

    </div>
  </header>

  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { onMounted, watchEffect } from 'vue';
import Navbar from './components/Navbar/Navbar.vue';
import "../public/styles.css"

import { useDarkModeStore } from './stores/darkMode';

const darkModeStore = useDarkModeStore()

watchEffect(() => {
  if (darkModeStore.isDarkMode) {
    document.body.classList.remove('body-light')
    document.body.classList.add('body-dark')
  } else if (!darkModeStore.isDarkMode) {
    document.body.classList.remove('body-dark')
    document.body.classList.add('body-light')
  }
}) 

</script>
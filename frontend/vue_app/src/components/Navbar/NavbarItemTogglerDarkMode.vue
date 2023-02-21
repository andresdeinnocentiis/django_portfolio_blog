<template>
    <div 
        class="darkMode-toggler-bar"
        :class="{'dark-theme-darkMode-toggler-bar':darkModeStore.isDarkMode, 'light-theme-darkMode-toggler-bar':!darkModeStore.isDarkMode}"
    >
        <div
            class="darkMode-toggler-btn"
            :class="{'dark-theme-btn':!darkModeStore.isDarkMode, 'light-theme-btn':darkModeStore.isDarkMode}"
            @click="toggleDarkMode"
        >
        <font-awesome-icon v-if="darkModeStore.isDarkMode" icon="fa-regular fa-sun" />
        <font-awesome-icon v-else icon="fa-regular fa-moon" />
        </div>
    </div>
    
</template>

<script setup>
import { useDarkModeStore } from "../../stores/darkMode";

const darkModeStore = useDarkModeStore()
const { toggleDarkMode } = darkModeStore

</script>
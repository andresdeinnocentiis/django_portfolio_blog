<template>
    <div  
        @click="toggleOpenMenu" 
        class="navMenu-toggler"
    >
        <div class="navicon-line line1" :class="{'navicon-line-dark':darkModeStore.isDarkMode, 'navicon-line-light':!darkModeStore.isDarkMode, 'line-closed-first': isMenuOpen}"></div>
        <div class="navicon-line line2" :class="{'navicon-line-dark':darkModeStore.isDarkMode, 'navicon-line-light':!darkModeStore.isDarkMode, 'line-closed-middle': isMenuOpen}"></div>
        <div class="navicon-line line3" :class="{'navicon-line-dark':darkModeStore.isDarkMode, 'navicon-line-light':!darkModeStore.isDarkMode, 'line-closed-last': isMenuOpen}"></div>
    </div>
</template>

<script setup>
import { useDarkModeStore } from '../../stores/darkMode';
import { useNavMenuStore } from '../../stores/navMenu';
import { storeToRefs } from 'pinia';

const darkModeStore = useDarkModeStore()
const navMenuStore = useNavMenuStore()
const { isMenuOpen } = storeToRefs(navMenuStore)
const { toggleOpenMenu } = navMenuStore

</script>
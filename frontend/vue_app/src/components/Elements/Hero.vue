<template>
    <div class="home-hero-section">
        <h1 class="home-hero__title">Andres De Innocentiis. <span class="dev-text">FullStack dev</span><span class="after-dev-text">_</span></h1>
        <p class="home-hero__text" :class="{'dark-theme-hero-text': isDarkMode, 'light-theme-hero-text': !isDarkMode}">I'm a FullStack web developer, lawyer and polyglot. In this site you'll find a blog section to check and review my projects.</p>
        <router-link :to="'/posts'" class="btn-cta-container">
            <div class="home-hero__btn-cta" :class="{'dark-theme-text': isDarkMode, 'light-theme-text': !isDarkMode}">
                <p 
                    class="hero-btn-text"
                    :class="{'hero-btn-text-light':!isDarkMode, 'hero-btn-text-dark':isDarkMode}"
                >Take a peek</p> 
            </div>
        </router-link>
    </div>
</template>


<script setup>
import { useDarkModeStore } from '../../stores/darkMode';
import { storeToRefs } from 'pinia';

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

</script>
<template>
    <footer 
        class="footer"
        :class="{'footer-dark':isDarkMode && forThisPage(), 'footer-light':!isDarkMode && forThisPage()}"
    >
        <div class="footer-container">
            <div class="footer-first-second">
                <div class="footer-first">
                    <h3 class="footer-title"><span class="footer-span">/</span>NNOKENTIY <span class="footer-span">&lt;</span>ODING.</h3>
                </div>
                <div class="footer-second">
                    <div class="footer-division">
                        <div class="division division1">
                            <h3>EXPLORE</h3>
                            <ul class="footer-explore">
                                <li><router-link :to="'/'" >Home</router-link></li>
                                <li><router-link :to="'/posts'" >Projects</router-link></li>
                                <li><router-link :to="'/about'" >About</router-link></li>
                                <li><router-link :to="'/contact'" >Contact</router-link></li>
                            </ul>
                        </div>
                        <div class="division division2">
                            <h3>FOLLOW</h3>
                            <ul class="footer-social-list">
                                <a href="https://www.linkedin.com/in/andresdeinnocentiis-pythondeveloper-webdeveloper/?locale=en_US" target="_blank"><li class="footer-social__link">
                                    <font-awesome-icon icon="fa-brands fa-linkedin" />
                                </li></a>
                                <a href="https://github.com/andresdeinnocentiis?tab=repositories" target="_blank"><li class="footer-social__link">
                                    <font-awesome-icon icon="fa-brands fa-github" />
                                </li></a>
                                <a href="https://www.instagram.com/andresdeinnocentiis/?hl=es-la" target="_blank"><li class="footer-social__link">
                                    <font-awesome-icon icon="fa-brands fa-instagram" />
                                </li></a>
                                <a href="mailto: andresdeinnocentiis@gmail.com" target="_blank"><li class="footer-social__link">
                                    <font-awesome-icon icon="fa-regular fa-envelope" />
                                </li></a>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="footer-last">Developed by me, <a href="https://www.linkedin.com/in/andresdeinnocentiis-pythondeveloper-webdeveloper/?locale=en_US" target="_blank">@andresdeinnocentiis</a> | &reg; 2023 Andres De Innocentiis</div>
        </div>
    </footer>
</template>

<script setup>
import { useDarkModeStore } from '../../stores/darkMode';
import { storeToRefs } from 'pinia';
import { watchEffect } from 'vue';
import { computed } from 'vue';
import { useRoute } from 'vue-router';

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

const route = useRoute()
const currentPage = computed(() => {
  return route.name;
});
console.log(currentPage.value);
const forThisPage = () => {
    let isForThisPage = false
    if (currentPage.value == 'home') {
        isForThisPage = true
    }
    return isForThisPage
}

</script>
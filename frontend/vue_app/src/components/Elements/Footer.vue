<template>
    <footer class="footer"
        :class="{'footer-dark':isDark, 'footer-light':!isDark}"
    >
        <div class="footer-container">
            <div class="footer-first-second">
                <div class="footer-first">
                    <h3 class="footer-title"><span class="footer-span">/</span>NNOKENTIY <span class="footer-span">&lt;</span>ODING .</h3>
                    <ul class="footer-social-list">
                        <a href="https://www.linkedin.com/in/andresdeinnocentiis-pythondeveloper-webdeveloper/?locale=en_US" target="_blank"><li class="footer-social__link">
                            <font-awesome-icon icon="fa-brands fa-linkedin" />
                        </li></a>
                        <a href="https://www.instagram.com/andresdeinnocentiis/?hl=es-la" target="_blank"><li class="footer-social__link">
                            <font-awesome-icon icon="fa-brands fa-instagram" />
                        </li></a>
                        <a href="mailto: andresdeinnocentiis@gmail.com" target="_blank"><li class="footer-social__link">
                            <font-awesome-icon icon="fa-regular fa-envelope" />
                        </li></a>
                        
                    </ul>
                </div>
                <div class="footer-second">
                    <h3>EXPLORE</h3>
                    <ul class="footer-explore">
                        <li><router-link :to="'/'" >Home</router-link></li>
                        <li><router-link :to="'/posts'" >Projects</router-link></li>
                        <li><router-link :to="'/about'" >About</router-link></li>
                        <li><router-link :to="'/resume'" >Resume</router-link></li>
                        <li><router-link :to="'/contact'" >Contact</router-link></li>
                    </ul>
                </div>
            </div>

            <div class="footer-last">Developed by me, <a href="https://www.linkedin.com/in/andresdeinnocentiis-pythondeveloper-webdeveloper/?locale=en_US" target="_blank">@andresdeinnocentiis</a> | &reg; 2023 Andres De Innocentiis</div>
        </div>
    </footer>
</template>

<script setup>
import { useDarkModeStore } from '../../stores/darkMode';
import { storeToRefs } from 'pinia';

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

</script>
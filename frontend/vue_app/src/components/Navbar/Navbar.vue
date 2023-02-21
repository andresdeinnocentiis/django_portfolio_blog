<template>
    <nav class="navbar">
      <div class="container">

        <div class="nav-mobile-container">

          <router-link 
            :to="{name: homeItem.routeName}" 
            exact 
            class="navbar-logo"
            :class="{'dark-theme-link':darkModeStore.isDarkMode, 'light-theme-link':!darkModeStore.isDarkMode}"
          >
            <span class="icon-logo-innokentiy-2" :class="{'dark-theme-logo':darkModeStore.isDarkMode, 'light-theme-logo':!darkModeStore.isDarkMode}"></span>
            <p class="logo-text" :class="{'dark-theme-link':darkModeStore.isDarkMode, 'light-theme-link':!darkModeStore.isDarkMode}">Innokentiy Coding .</p>
          </router-link> 

          <div class="navbar-toggler" :class="{'toggler-absolute': isMenuOpen}">
            <NavbarTogglerIcon />
          </div>

        </div>

        <div 
          class="collapse navbar-collapse"
          :class="{'navbar-open': isMenuOpen, 'navbar-open-dark': isDarkMode, 'navbar-open-light': !isDarkMode}"  
        >
          <ul 
            class="navbar-nav" 
            :class="{'nav-open': isMenuOpen, 'navbar-open-dark': isDarkMode, 'navbar-open-light': !isDarkMode}"  
          >
            <NavbarItemTogglerDarkMode />
            <NavbarItem :item="item" v-for="(item, index) in navItems" :key="index" />
            <NavbarItemLogin />
            
          </ul>
        </div>
      </div>
    </nav>
</template>

<script setup>
import NavbarItem from './NavbarItem.vue';
import NavbarItemLogin from './NavbarItemLogin.vue';
import NavbarItemTogglerDarkMode from './NavbarItemTogglerDarkMode.vue';
import NavbarTogglerIcon from './NavbarTogglerIcon.vue';
import { storeToRefs } from 'pinia';
import { useNavMenuStore } from '../../stores/navMenu';
import { useDarkModeStore } from '../../stores/darkMode';

const darkModeStore = useDarkModeStore()
const navMenuStore = useNavMenuStore()
const { isDarkMode } = storeToRefs(darkModeStore)
const { isMenuOpen } = storeToRefs(navMenuStore)


const homeItem = {name: "Home", routeName:"home"}

const navItems = [
          {name: "About", routeName:"about"},
          {name: "Projects", routeName:"posts"},
          {name: "Resume", routeName:"resume"},
          {name: "Contact", routeName:"contact"},
]


</script>
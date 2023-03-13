<template>
    <div 
        class="login-nav-items last-nav-item"
        :class="{'dark-theme-last-nav-item':darkModeStore.isDarkMode, 'light-theme-last-nav-item':!darkModeStore.isDarkMode}"
        v-if="isUserLogged()"
    >
        <li class="nav-item-username">
        <p 
            :class="{'dark-theme-link':darkModeStore.isDarkMode, 'light-theme-link':!darkModeStore.isDarkMode}"
        >Welcome, </p><a 
                        class="nav-link" 
                        href="#"
                        :class="{'dark-theme-link':darkModeStore.isDarkMode, 'light-theme-link':!darkModeStore.isDarkMode}"
                    >{{userLoggedStore.userInfo.username}}</a>
        </li>
        <li class="nav-item-logout" :class="{'dark-theme-nav-item-logout':darkModeStore.isDarkMode, 'light-theme-nav-item-logout':!darkModeStore.isDarkMode}">
        <a 
            href="#" 
            @click="handleLogout" 
            class="btn-logout"
        >
            <font-awesome-icon icon="fa-solid fa-power-off" :class="{'dark-theme-link-power-off':darkModeStore.isDarkMode, 'light-theme-link-power-off':!darkModeStore.isDarkMode}" />
        </a>
        </li>
    </div>
    <div v-else>
        <li 
            class="nav-item-login last-nav-item"
            :class="{'dark-theme-last-nav-item':darkModeStore.isDarkMode, 'light-theme-last-nav-item':!darkModeStore.isDarkMode}"
        >    
            <router-link :to="{name: 'login'}" :class="{'dark-theme-link':darkModeStore.isDarkMode, 'light-theme-link':!darkModeStore.isDarkMode}">
                Login / Register
            </router-link> 
        </li>
    </div>
</template>

<script setup>
import { useUserLoggedStore } from "../../stores/userLogged"
import { useDarkModeStore } from '../../stores/darkMode';

const darkModeStore = useDarkModeStore()

const userLoggedStore = useUserLoggedStore() 

const { login, logout, isUserLogged, loadUserInfo } = userLoggedStore

const handleLogout = () => {
    logout()
    isUserLogged()
    loadUserInfo()
}

</script>
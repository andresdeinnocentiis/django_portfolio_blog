<template>
    <div class="login_container">
        <div class="section_container">
            <h1 
                class="sec-sect-title login-title"
                :class="{'title-dark': isDarkMode, 'title-light': !isDarkMode}"
            >Login</h1>
    
            <LoginForm />
        </div>
    </div>
</template>

<script setup>
import LoginForm from '../components/Login/LoginForm.vue';
import { useDarkModeStore } from '../stores/darkMode';
import { storeToRefs } from 'pinia';

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)



</script>
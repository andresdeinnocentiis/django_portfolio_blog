<template>
    <form 
        class="login-form"
        :class="{'login-form-dark': isDarkMode, 'login-form-light': !isDarkMode}"
    >
    <Message v-if="error" :variant="'danger'" :message="error" />
        <div class="inputs-container">
            <label class="custom-field" aria-label="Enter username">
                <input v-model="username" type="text" :class="{'input-form-dark': isDarkMode, 'input-form-light': !isDarkMode}" required placeholder="&nbsp;"/>
                <span class="placeholder">Enter Username</span>
            </label>

            <label class="custom-field" aria-label="Enter password">
                <input v-model="password" type="password" :class="{'input-form-dark': isDarkMode, 'input-form-light': !isDarkMode}" required placeholder="&nbsp;"/>
                <span class="placeholder">Enter Password</span>
            </label>
        </div>
        <div class="form-btn-container">
            <button 
            type="submit"
                class="form-btn" 
                :class="{'light-theme-text': isDarkMode, 'dark-theme-text': !isDarkMode}"
                @click.prevent="handleLogin()"    
            >Login</button>
            <p :class="{'light-theme-text': isDarkMode, 'dark-theme-text': !isDarkMode}">Not a user yet? <router-link :to="'/register'" :class="{'light-theme-text': isDarkMode, 'dark-theme-text': !isDarkMode}" class="sign-in">Sign in!</router-link></p>
        </div>
    </form>
</template>

<script setup>
import { useDarkModeStore } from '../../stores/darkMode';
import { useUserLoggedStore } from '../../stores/userLogged';
import { storeToRefs } from 'pinia';
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Message from '../Elements/Message.vue';

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

const userLoggedStore = useUserLoggedStore()
const { userInfo, logging } = storeToRefs(userLoggedStore)
const { login } = userLoggedStore

const router = useRouter()

const error = ref("");

let username = ref("")
let password = ref("")


const handleLogin = async () => {
    if (!username.value) {
        error.value = "Username can't be empty."
    } else if (!password.value) {
        error.value = "Password can't be empty."
    } else {
        
        try {
            const success = await login(username.value, password.value)
            
            if (success) {
                username.value = ""
                password.value = ""
                error.value = ""
                router.push({name: 'home'})

            } else {
                
                error.value = "Invalid username or password"         
            }

        } catch {
            error.value = "An error occured during login."
        }
    }
        
        
    


    
    

}

</script>
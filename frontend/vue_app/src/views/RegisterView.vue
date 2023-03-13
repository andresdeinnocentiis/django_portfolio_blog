<template>
    <div class="contact-form-container">
        <h1 class="contact-form-title">Register</h1>
        <form class="contact-form form-modal" @submit.prevent="handleRegister">
            
            <Message v-if="error" :variant="'danger'" :message="error" />

            <p class="input-error" v-if="!isUsernameValid">{{inputErrors.username}}</p>
            <label class="custom-field input-form-light" aria-label="Enter your name">
                <input class="input-form-light" v-model="username" type="text" required placeholder="&nbsp;"/>
                <span class="placeholder placeholder-modal contact-form-placeholder">Enter Username</span>
            </label>

            <p class="input-error" v-if="!isEmailValid">{{inputErrors.email}}</p>
            <label class="custom-field input-form-light " aria-label="Enter your email">
                <input class="input-form-light" v-model="email" type="email" required placeholder="&nbsp;"/>
                <span class="placeholder placeholder-modalcontact-form-placeholder contact-form-placeholder">Enter Email</span>
            </label>
            
            <p class="input-error" v-if="!isPasswordValid">{{inputErrors.password}}</p>
            <label class="custom-field input-form-light" aria-label="Enter your password">
                <input class="input-form-light" v-model="password" type="password" required placeholder="&nbsp;"/>
                <span class="placeholder placeholder-modal contact-form-placeholder">Enter Password</span>
            </label>

            <p class="input-error" v-if="!passwordsMatch">{{inputErrors.confirmPassword}}</p>
            <label class="custom-field input-form-light" aria-label="Enter your password">
                <input class="input-form-light" v-model="confirmPassword" type="password" required placeholder="&nbsp;"/>
                <span class="placeholder placeholder-modal contact-form-placeholder">Confirm Password</span>
            </label>

            <label class="custom-field input-form-light" aria-label="Enter your linkedin">
                <input class="input-form-light" v-model="linkedin" type="text" required placeholder="&nbsp;"/>
                <span class="placeholder placeholder-modal contact-form-placeholder">Enter Linkedin account</span>
            </label>
            <div class="contact-form-btns-container register-btns">
                <button class="contact-send" type="submit">Register</button>
                <button class="contact-reset" type="reset">Reset</button>
                <p class="already-user">Already a user? <router-link :to="'/login'" >Log in!</router-link></p>
            </div>

        </form>
        <ProcessingRequest 
            v-if="loading" 
            :text="'Your account is being created. Please wait..'"    
        />
        <TransactionModal 
            v-if="showSuccess" 
            :success="true"
            :title="'Success!'"
            :message="'You have been registered successfully!'"
            :variant="'success'"
        />
    </div>
</template>
  
<script setup>
import { ref, watch } from 'vue';
import { storeToRefs } from 'pinia';
import { useModalStore } from '../stores/modal';
import { useUserLoggedStore } from '../stores/userLogged';
import { getAPI } from '../axios-api';
import ProcessingRequest from '../components/Elements/ProcessingRequest.vue';
import TransactionModal from '../components/Elements/TransactionModal.vue';
import Message from '../components/Elements/Message.vue';

const modalStore = useModalStore()
const { tsxHiddenClass } = storeToRefs(modalStore)
const { toggleTsxModal } = modalStore

const userLoggedStore = useUserLoggedStore()
const { createUser } = userLoggedStore

const error = ref("")

const username = ref('');
const password = ref('');
const confirmPassword = ref('');
const email = ref('');
const linkedin = ref('');


const loading = ref(false)
const showSuccess = ref(false)

const isUsernameValid = ref(true);
const isPasswordValid = ref(true);
const passwordsMatch = ref(true)
const isEmailValid = ref(true);


const inputErrors = ref({
    username: '',
    password: '',
    confirmPassword: '',
    email: ''
})

// Functions for validations:
const isValidUsername = (username) => {
    const regex = /^[a-zA-Z0-9_@.+\\-]{3,25}$/; // This regex requires the username to have at least 3 characters and only allow letters, numbers, dots, underscores, and hyphens.
    return regex.test(username); // Test is a built-in function in JavaScript used to test if a given string matches a regular expression
}

const isValidPassword = (password) => {
    const regex = /^(?=.*[a-zA-Z0-9])(?=.*[-+.@_])[a-zA-Z0-9-+.@_]{8,}$/;
    return regex.test(password);
}


const handleRegister = async () => {
    try {
        loading.value = true
        const userExists = await getAPI.get('/api/users/username_exists/', {
            params: {
                username: username
            }
        })
        /*const emailExists = await getAPI.get('/api/users/email_exists/', {
            params: {
                email: email
            }
        })*/

        if (userExists.data["username_exists"]) {
            error.value = "Username already exists."
        } /*else if (emailExists.data["email_exists"]) {
            error.value = "The email is already registered in the Database."
        }*/ else if (!username.value) {
        error.value = "Username can't be empty."
        } else if (!password.value) {
            error.value = "Password can't be empty."
        } else if (!email.value) {
            error.value = "Email can't be empty."
        } else if (isUsernameValid && isPasswordValid && isEmailValid && passwordsMatch){
            
            const userData = {
                username: username.value,
                password: password.value,
                email: email.value,
                linkedin: linkedin.value ? linkedin.value : null
            }

            console.log("USER DATA: ", userData);
            
            const response = await createUser(userData)

            if (response.data) {
                loading.value = false
                toggleTsxModal()
                showSuccess.value = true
                username.value = ""
                email.value = ""
                password.value = ""
                linkedin.value = ""
                setTimeout(() => {
                    showSuccess.value = false
                    toggleTsxModal()
                },3000)
            }
        }

    } catch (error) {
        console.error(error);
        console.log(error.response)
        alert('An error occurred. Please try again later.');
    }
};


// WATCHERS: (INPUT VALIDATORS)

watch(username, (newValue) => {
    if (newValue.length < 3) {
        isUsernameValid.value = false;
        inputErrors.value.username = "Username must be at least 3 characters long."
    } else if (!isValidUsername(newValue)) {
        isUsernameValid.value = false;
        inputErrors.value.username = "Username can only contain letters, numbers, dots, underscores, and hyphens."
    } else {
        isUsernameValid.value = true
        inputErrors.value.username = ""
    }
});

watch(password, (newValue) => {
    if (newValue.length < 8) {
        isPasswordValid.value = false;
        inputErrors.value.password = "Password must be at least 8 characters long."
    } else if (!isValidPassword(newValue)) {
        isPasswordValid.value = false;
        inputErrors.value.password = "Password must contain at least one alphanumeric character and one of the special characters '-, +, ., @, or _'."
    } else {
        isPasswordValid.value = true
        inputErrors.value.password = ""
    }
});

watch(confirmPassword, (newValue) => {
    if (newValue !== password.value) {
        passwordsMatch.value = false;
        inputErrors.value.confirmPassword = "Passwords don't match."
    } else {
        passwordsMatch.value = true
        inputErrors.value.confirmPassword = ""
    }
});

watch(email, (newValue) => {
    const regex = /\S+@\S+\.\S+/;
    if (regex.test(newValue)) {
      isEmailValid.value = true;
      inputErrors.value.email = ""
    } else {
      isEmailValid.value = false;
      inputErrors.value.email = "Invalid email."
    }
});
</script>
  
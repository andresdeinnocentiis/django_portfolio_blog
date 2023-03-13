<template>
    <div class="contact-form-container">
        <h1 class="contact-form-title">Contact me</h1>
        <form class="contact-form form-modal" @submit.prevent="sendEmail">
            
            <label class="custom-field input-form-light" aria-label="Enter your name">
                <input class="input-form-light" v-model="name" type="text" required placeholder="&nbsp;"/>
                <span class="placeholder placeholder-modal contact-form-placeholder">Enter Name</span>
            </label>
            <label class="custom-field input-form-light " aria-label="Enter your email">
                <input class="input-form-light" v-model="email" type="email" required placeholder="&nbsp;"/>
                <span class="placeholder placeholder-modalcontact-form-placeholder contact-form-placeholder">Enter Email</span>
            </label>
            <label class="custom-field input-form-light" aria-label="Enter your subject">
                <input class="input-form-light" v-model="subject" type="text" required placeholder="&nbsp;"/>
                <span class="placeholder placeholder-modal contact-form-placeholder">Enter subject</span>
            </label>
            <label class="custom-field input-form-light" aria-label="Enter techs used">
                <textarea style="resize: none;" class="input-form-light" v-model="message" type="text" required placeholder="&nbsp;" rows="14" cols="50"/>
                <span class="placeholder-textarea contact-form-placeholder">Type Message</span>
            </label>
            <div class="contact-form-btns-container">
                <button class="contact-send" type="submit">Send</button>
                <button class="contact-reset" type="reset">Reset</button>
            </div>

        </form>
        <ProcessingRequest 
            v-if="loading" 
            :text="'Your email is being sent. Please wait..'"    
        />
        <TransactionModal 
            v-if="showSuccess" 
            :success="true"
            :title="'Success!'"
            :message="'Your email was sent successfully!'"
            :variant="'success'"
        />
    </div>
</template>
  
<script setup>
import { storeToRefs } from 'pinia';
import { ref } from 'vue';
import { getAPI } from '../axios-api';
import ProcessingRequest from '../components/Elements/ProcessingRequest.vue';
import TransactionModal from '../components/Elements/TransactionModal.vue';
import { useModalStore } from '../stores/modal';

const modalStore = useModalStore()
const { tsxHiddenClass } = storeToRefs(modalStore)
const { toggleTsxModal } = modalStore


const name = ref('');
const email = ref('');
const subject = ref('');
const message = ref('');
const loading = ref(false)
const showSuccess = ref(false)

const sendEmail = async () => {
    try {
        loading.value = true
        const response = await getAPI.post('/api/send_email/', {
        name: name.value,
        email: email.value,
        subject: subject.value,
        message: message.value
        }, { timeout: 10000 });

        loading.value = false
        toggleTsxModal()
        showSuccess.value = true
        name.value = ""
        email.value = ""
        subject.value = ""
        message.value = ""
        setTimeout(() => {
            showSuccess.value = false
            toggleTsxModal()
        },3000)


    } catch (error) {
        console.error(error);
        console.log(error.response)
        alert('An error occurred. Please try again later.');
    }
};
</script>
  
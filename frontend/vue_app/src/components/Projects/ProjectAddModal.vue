<template>
    <div class="modal-project-add-overlay" :class="hiddenClass">
        <div class="modal-project-add">
            <font-awesome-icon icon="fa-solid fa-xmark" class="close-modal" @click.prevent="toggleProjectModal"/>
            <div class="form-modal-container">
                <h3 class="form-title light-theme-text">Add a new Project</h3>
                <form class="form-modal">
                    <transition name="fade">
                        <Message class="modal-message" v-if="errorMsg" :variant="'danger'" :message="errorMsg" />
                    </transition>
                    <transition name="fade">    
                        <Message class="modal-message" v-if="successMsg" :variant="'success'" :message="successMsg" />
                    </transition>
                    <div class="inputs-container inputs-container-modal">
                        <label class="custom-field input-form-dark" aria-label="Enter title">
                            <input class="input-form-dark" v-model="title" type="text" required placeholder="&nbsp;"/>
                            <span class="placeholder placeholder-modal">Enter Title</span>
                        </label>
            
                        <label class="custom-field input-form-dark" aria-label="Enter caption">
                            <input class="input-form-dark" v-model="caption" type="text" required placeholder="&nbsp;"/>
                            <span class="placeholder placeholder-modal">Enter Caption</span>
                        </label>

                        <label class="custom-field input-form-dark" aria-label="Upload image">
                            <input class="input-form-dark dark-theme-text" @change="setImage" type="file" accept="image/*" required placeholder="&nbsp;"/>
                        </label>

                        <label class="custom-field input-form-dark" aria-label="Enter description">
                            <textarea style="resize: none;" class="input-form-dark" v-model="description" type="text" required placeholder="&nbsp;" rows="4" cols="50"/>
                            <span class="placeholder-textarea">Enter Description</span>
                        </label>

                        <label class="custom-field input-form-dark" aria-label="Enter techs used">
                            <textarea style="resize: none;" class="input-form-dark" v-model="tech_used" type="text" required placeholder="&nbsp;" rows="4" cols="50"/>
                            <span class="placeholder-textarea">Enter Techs Used</span>
                        </label>

                        <label class="custom-field input-form-dark" aria-label="Enter developed for">
                            <input class="input-form-dark" v-model="developed_for" type="text" required placeholder="&nbsp;"/>
                            <span class="placeholder placeholder-modal">Enter Developed For</span>
                        </label>

                        <label class="custom-field input-form-dark" aria-label="Enter Developed for Link">
                            <input class="input-form-dark" v-model="developed_for_link" type="url" required placeholder="&nbsp;"/>
                            <span class="placeholder placeholder-modal">Enter Developed For Link</span>
                        </label>
                        <label class="custom-field input-form-dark" aria-label="Enter Github link">
                            <input class="input-form-dark" v-model="github_link" type="url" required placeholder="&nbsp;"/>
                            <span class="placeholder placeholder-modal">Enter Github link</span>
                        </label>

                        <label class="custom-field input-form-dark" aria-label="Enter Website link">
                            <input class="input-form-dark" v-model="website_link" type="url" required placeholder="&nbsp;"/>
                            <span class="placeholder placeholder-modal">Enter Website link</span>
                        </label>
                    </div>
                    <div class="form-btn-container">
                        <button 
                            type="submit"
                            class="form-btn" 
                            @click.prevent="handleSubmit()"    
                        >Add Project</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { ref } from 'vue'
import { useModalStore } from '../../stores/modal';
import { usePostsStore } from "../../stores/posts"
import Message from '../Elements/Message.vue';


const modalStore = useModalStore()
const { hiddenClass } = storeToRefs(modalStore)
const { toggleProjectModal } = modalStore


const postsStore = usePostsStore()
const { postPost }  = postsStore

const errorMsg = ref("");

const successMsg = ref("")

let title = ref("")
let caption = ref("")
let image = ref(null)
let description = ref("")
let tech_used = ref("")
let developed_for = ref("")
let developed_for_link = ref("")
let github_link = ref("")
let website_link = ref("")

const setImage = (e) => {
    image.value = e.target.files[0]
}

const showSuccess = (success) => {
    console.log("SUCCESS?", success);
    if (success) {
        successMsg.value = "The Project has been added successfully!"
    
        setTimeout(() => {
                successMsg.value = ""
                toggleProjectModal()
            }, 3000)
    } else {
        errorMsg.value = "There was a problem adding the Project. Please try again."
    
        setTimeout(() => {
                errorMsg.value = ""
            }, 3000)
    }
    
    
}


const handleSubmit = async () => {   

    let formData = new FormData();
    formData.append('title', title.value);
    formData.append('caption', caption.value);
    formData.append('image', image.value);
    formData.append('description', description.value);
    formData.append('tech_used', tech_used.value);
    formData.append('developed_for', developed_for.value);
    formData.append('developed_for_link', developed_for_link.value);
    formData.append('github_link', github_link.value);
    formData.append('website_link', website_link.value);

    

    try {
        const success = await postPost(formData)
        if (success) {
            showSuccess(success)
        } else { 
            showSuccess(success)
        }

    } catch(error) {
        console.log(error);
    } finally {
        title.value = ""
        caption.value = ""
        image.value = null
        description.value = ""
        tech_used.value = ""
        developed_for.value = ""
        developed_for_link.value = ""
        github_link.value = ""
        website_link.value = ""
    }
}
</script>

<style>
    .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
    }
    .fade-enter, .fade-leave-to {
    opacity: 0;
    }
</style>

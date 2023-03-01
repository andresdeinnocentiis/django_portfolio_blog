<template>
    <div class="modal-project-add-overlay" :class="editHiddenClass">
        <div class="modal-project-add">
            <font-awesome-icon icon="fa-solid fa-xmark" class="close-modal" @click.prevent="handleCloseEdit"/>
            <div class="form-modal-container">
                <h3 class="form-title light-theme-text">Edit Project</h3>
                <form class="form-modal">
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

                        <label class="custom-field input-form-dark" aria-label="Enter Status">
                            <input class="input-form-dark" v-model="status" type="text" required placeholder="&nbsp;"/>
                            <span class="placeholder placeholder-modal">Enter Status</span>
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
                        >Confirm Edit</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

  
    <TransactionModal 
        :variant="editModalMsg.variant" 
        :title="editModalMsg.title" 
        :message="editModalMsg.msg" 
        :success="editModalMsg.success"
    />

</template>

<script setup>
import { storeToRefs } from 'pinia';
import { ref } from 'vue'
import { useModalStore } from '../../stores/modal';
import { usePostsStore } from "../../stores/posts"


const modalStore = useModalStore()
const { editHiddenClass } = storeToRefs(modalStore)
const { toggleEditProjectModal } = modalStore


const postsStore = usePostsStore()
const { updatePost, getPostDetails }  = postsStore
const { currentPost } = storeToRefs(postsStore)




const editModalMsg = ref({
    title: "",
    msg: "",
    variant: "",
    success: false
})

let title = ref(currentPost.value.title)
let caption = ref(currentPost.value.caption)
let image = ref(currentPost.value.image)
let description = ref(currentPost.value.description)
let tech_used = ref(currentPost.value.tech_used)
let developed_for = ref(currentPost.value.developed_for)
let developed_for_link = ref(currentPost.value.developed_for_link)
let status = ref(currentPost.value.status)
let github_link = ref(currentPost.value.github_link)
let website_link = ref(currentPost.value.website_link)

const setImage = (e) => {
    image.value = e.target.files[0]
}



const handleSubmit = async () => {   

    let formData = new FormData();
    formData.append('title', title.value);
    formData.append('caption', caption.value);
    if (image.value) {
        formData.append('image', image.value);
    }
    formData.append('description', description.value);
    formData.append('tech_used', tech_used.value);
    formData.append('developed_for', developed_for.value);
    formData.append('developed_for_link', developed_for_link.value);
    formData.append('status', status.value);
    formData.append('github_link', github_link.value);
    formData.append('website_link', website_link.value);

    

    try {
        const success = await updatePost(currentPost.value.id, formData)
        if (success) {
            editModalMsg.value.success = true
            editModalMsg.value.variant = "success"
            editModalMsg.value.title = "Success!"
            editModalMsg.value.msg = "The project was updated successfully!"

            getPostDetails(currentPost.value.id)

            setTimeout(() => {
                toggleEditProjectModal()
                editModalMsg.value.success = false
                editModalMsg.value.variant = ""
                editModalMsg.value.title = ""
                editModalMsg.value.msg = ""
            }, 2000)
        } else { 
            editModalMsg.value.success = false
            editModalMsg.value.variant = "danger"
            editModalMsg.value.title = "Error."
            editModalMsg.value.msg = "There was a problem updating the Project. Please try again."

            setTimeout(() => {
                toggleEditProjectModal()
                editModalMsg.value.success = false
                editModalMsg.value.variant = ""
                editModalMsg.value.title = ""
                editModalMsg.value.msg = ""
            }, 2000)
        }

    } catch(error) {
        console.log(error);
    } 
}

// When I close the modal if I did any modifications without confirming, the data should be back to it's original state
const handleCloseEdit = () => {
    toggleEditProjectModal()
    title = currentPost.value.title
    caption = currentPost.value.caption
    image = currentPost.value.image
    description = currentPost.value.description
    tech_used = currentPost.value.tech_used
    developed_for = currentPost.value.developed_for
    developed_for_link = currentPost.value.developed_for_link
    status = currentPost.value.status
    github_link = currentPost.value.github_link
    website_link = currentPost.value.website_link
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

<template>
    
    <div class="posts_container">
        <h1 class="posts__title">Projects</h1>
        <AddButton v-if="isUserAdmin" :btnName="'project'" :color="'#FF435E'" @click.prevent="toggleProjectModal"/>
        <div class="posts-container">
            <ProjectCard 
                class="post"
                v-for="post in postsStore.listPosts"
                :key="post.id"
                :project="post"
            />
        </div>   

    </div>
    <!-- Add Project [Modal] -->
    <ProjectAddModal />
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { usePostsStore } from "../stores/posts"
import { useUserLoggedStore } from "../stores/userLogged";
import { useModalStore } from "../stores/modal";
import ProjectAddModal from '../components/Projects/ProjectAddModal.vue';

import ProjectCard from "../components/Projects/ProjectCard.vue";
import AddButton from "../components/Elements/AddButton.vue";

const postsStore = usePostsStore()
const userLoggedStore = useUserLoggedStore()
const {isUserAdmin} = storeToRefs(userLoggedStore)
const modalStore = useModalStore()
const { toggleProjectModal } = modalStore



const { getPosts } = postsStore

getPosts()



</script>
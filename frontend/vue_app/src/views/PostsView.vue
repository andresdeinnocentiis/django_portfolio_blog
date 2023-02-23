<template>
    
    <div class="posts_container">
        <h1 class="posts__title">Posts View</h1>
        <div class="posts-container">
            <ProjectCard 
                class="post"
                v-for="post in postsStore.listPosts"
                :key="post.id"
                :project="post"
            />
        </div>   

    </div>
</template>

<script setup>
import { usePostsStore } from "../stores/posts"
import ProjectCard from "../components/Projects/ProjectCard.vue";

const postsStore = usePostsStore()

const { getPosts } = postsStore

getPosts()



</script>
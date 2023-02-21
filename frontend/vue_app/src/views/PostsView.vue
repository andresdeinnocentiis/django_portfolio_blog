<template>
    
    <div class="posts_container">
        <h1>Posts View</h1>
        <div class="posts-container">
            <div 
                class="post"
                v-for="post in postsStore.listPosts"
                :key="post.id"
            >
            {{ post.title }}
            </div>
        </div>
    </div>
</template>

<script setup>

import { usePostsStore } from "../stores/posts"



const postsStore = usePostsStore()

const { getPosts } = postsStore

getPosts()



</script>
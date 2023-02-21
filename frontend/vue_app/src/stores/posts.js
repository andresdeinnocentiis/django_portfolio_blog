import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { getAPI } from '../axios-api';

export const usePostsStore = defineStore("getPosts", () => {
  
    const listPosts = ref([]) 

    const getPosts = async () => {
        console.log("INICIA GET POSTS");
        try {
            const response = await getAPI.get('/api/posts/get/')
            console.log("RESPONSE: ", response.data);
            if (response.data) {
            // Update the store state with the logged in user's information
                const posts = response.data
                listPosts.value = posts
                console.log("listPosts: ", listPosts.value);
                // Save the posts info to local storage
                localStorage.setItem('listPosts', JSON.stringify(posts))
            } else {
                // Handle login failure
                listPosts.value = []
                // Throw an error or display an error message to the user
                throw new Error('Login failed. Please try again.')
            }

        } catch(error) { 
            console.error("ERROR: ", error);
        } 

    }
  
  return { listPosts, getPosts }
});

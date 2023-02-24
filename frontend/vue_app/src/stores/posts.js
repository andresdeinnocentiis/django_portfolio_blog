import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { getAPI } from '../axios-api';

export const usePostsStore = defineStore("getPosts", () => {
  
    const listPosts = ref([]) 

    const getPosts = async () => {

        try {
            const response = await getAPI.get('/api/posts/get/')

            if (response.data) {
            // Update the store state with the posts' information
                const posts = response.data
                listPosts.value = posts
                // Save the posts info to local storage
                localStorage.setItem('listPosts', JSON.stringify(posts))
            } else {
                // Handle failure
                listPosts.value = []
                // Throw an error or display an error message to the user
                throw new Error('Failed getting the posts. Please try again.')
            }

        } catch(error) { 
            console.error("ERROR: ", error);
        } 

    }
  
  return { listPosts, getPosts }
});

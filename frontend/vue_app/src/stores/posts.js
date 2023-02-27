import { ref } from 'vue'
import { defineStore, storeToRefs } from 'pinia'
import { v4 as uuidv4 } from 'uuid'
import { useUserLoggedStore } from './userLogged'
import { getAPI } from '../axios-api';

export const usePostsStore = defineStore("getPosts", () => {
    
    const userLoggedStore = useUserLoggedStore()
    const { userInfo } = storeToRefs(userLoggedStore)

    const listPosts = ref([{}]) 
    const currentPost = ref({})


    const isPostLikedByUser = ref(false)

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

    const getPostDetails = async (id) => {

        try {
            const response = await getAPI.get(`/api/posts/${id}/get/`)

            if (response.data) {
            // Update the store state with the posts' information
                const post = response.data

                currentPost.value = post
                // Save the post info to local storage
                localStorage.setItem('currentPost', JSON.stringify(post))
                
            } else {
                // Handle failure
                currentPost.value = {}
                // Throw an error or display an error message to the user
                throw new Error('Failed getting the post. Please try again.')

            }

        } catch(error) { 
            console.error("ERROR: ", error);

        } 

    }

    const getIsPostLikedByUser = async (postId, user) => {
        let isLiked = false
        let identifier

        if (user.value.anonymousIdentifier) {
            identifier = user.value.anonymousIdentifier
            try {
                const response = await getAPI.get(`/api/posts/${postId}/is_liked/anonymous_user/${identifier}/`, {})
                const likeArray = response.data
                
                if (likeArray.length > 0) {
                    const like = likeArray[0]
    
                    if(like.post == postId && (like.anonymous_identifier == identifier)) {
                        isLiked = true
                    }
                } else {
                    isLiked = false
                }
                
                isPostLikedByUser.value = isLiked        
            } catch(error) {
                console.log(error);
            }
        } else {

            identifier = user.value.id

            try {
                const response = await getAPI.get(`/api/posts/${postId}/is_liked/user/${identifier}/`, {})
                const likeArray = response.data
  
                if (likeArray.length > 0) {
                    const like = likeArray[0]
    
                    if(like.post == postId && (like.user == identifier)) {
                        isLiked = true
                        isPostLikedByUser.value = isLiked 
                    }
                } else {
                    isLiked = false
                }
                
                isPostLikedByUser.value = isLiked        
            } catch(error) {
                console.log(error);
            }
        }
    }
    
        

    const postPost = async (project) => {
        try {
            const response = await getAPI.post('api/posts/post/', project, {
            headers: {
                'Content-Type': 'multipart/form-data',
                Authorization: `Bearer ${userInfo.value.token}`
            }
            });

            // Now we update the PostsView:
            getPosts()

            return true
        } catch (error) { 
            console.log(error);
            console.error(error);
            return false
        }
    }


  
  return { listPosts, currentPost, getPosts, getPostDetails, postPost, getIsPostLikedByUser, isPostLikedByUser }
});

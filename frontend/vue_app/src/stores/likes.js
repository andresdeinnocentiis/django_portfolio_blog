import { ref } from 'vue'
import { defineStore, storeToRefs } from 'pinia'
import { getAPI } from '../axios-api';


export const useLikesStore = defineStore("likesStore", () => {
 
    const likesList = ref(null) 
    const currentPostLikeId = ref(null)

    const getLikes = async () => {

        try {
            const response = await getAPI.get('/api/likes/get/')

            if (response.data) {
                // Update the store state with the posts' information
                const likes = response.data
                likesList.value = likes
                // Save the likes info to local storage
                localStorage.setItem('likesList', JSON.stringify(likes))
            } else {
                // Handle failure
                likesList.value = [{}]
                // Throw an error or display an error message to the user
                throw new Error('Failed getting the likes. Please try again.')
            }
        } catch (error) {
            console.log(error)
        }
    }

    const getUserLikeForPost = async (postId, user) => {
        let likeId = false
        let identifier

        if (user.value.anonymousIdentifier) {
            identifier = user.value.anonymousIdentifier
            try {
                const response = await getAPI.get(`/api/likes/post/${postId}/anonymous_user/${identifier}/get/`, {})
                const likeArray = response.data
                
                if (likeArray.length > 0) {
                    const like = likeArray[0]
    
                    if(like.post == postId && (like.anonymous_identifier == identifier)) {
                        likeId = like.id
                    }
                } else {
                    likeId = null
                }
                
                currentPostLikeId.value = likeId        
            } catch(error) {
                console.log(error);
            }
        } else {

            identifier = user.value.id

            try {
                const response = await getAPI.get(`/api/likes/post/${postId}/user/${identifier}/get/`, {})
                const likeArray = response.data
  
                if (likeArray.length > 0) {
                    const like = likeArray[0]
    
                    if(like.post == postId && (like.user == identifier)) {
                        likeId = like.id 
                    }
                } else {
                    likeId = null
                }
                
                currentPostLikeId.value = likeId        
                console.log("CURRENT LIKE ID: ", currentPostLikeId.value);
            } catch(error) {
                console.log(error);
            }
        }
    }

    const postLike = async (like) => {
        try {
            const response = await getAPI.post('/api/likes/post/', like, {
            headers: {
                'Content-Type': 'application/json',
            }
            });

            if (response.status === 201) {
                // Now we update the Likes 
                getLikes()

            }

            return true
        } catch (error) { 
            console.log(error);
            return false
        }
    }
    
    const deleteLike = async (likeId) => {
        try {
            const response = await getAPI.delete(`/api/likes/${likeId}/delete/`, {
                headers: {
                    'Content-Type': 'application/json',
                }
            })

            
            // Now we update the Likes:
            getLikes()

            

            return true
        } catch (error) {
            console.log(error);
 
            return false
        }
    }

    return { likesList, getLikes, postLike, deleteLike, getUserLikeForPost, currentPostLikeId }
})

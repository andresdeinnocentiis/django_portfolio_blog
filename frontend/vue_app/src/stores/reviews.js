import { ref } from 'vue'
import { defineStore, storeToRefs } from 'pinia'
import { useUserLoggedStore } from './userLogged'
import { getAPI } from '../axios-api';

export const useReviewsStore = defineStore('reviewsStore', () => {

    const userLoggedStore = useUserLoggedStore()
    const { userInfo } = storeToRefs(userLoggedStore)

    const reviewsList = ref([{}]) 
    const currentPostReviews = ref([{}])

    const userReviewsForPost = ref([{}])



    // GET Method to retrieve all the Reviews:
    const getReviews = async () => {
        try {
            const response = await getAPI.get('/api/reviews/get/')

            if(response.data) {
                const reviews = response.data

                reviewsList.value = reviews
                // Save the reviews info to local storage
                localStorage.setItem('reviewsList', JSON.stringify(reviews))

                return true
            } else {
                // Handle failure
                reviewsList.value = [{}]
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error)
        }
    }

    // GET Method to retrieve all the Reviews for a specific Post:
    const getReviewsForPost = async (postId) => {

        try {

            const response = await getAPI.get(`/api/reviews/post/${postId}/get/`)

            if (response.data) {
                const postReviews = response.data

                currentPostReviews.value = postReviews

                // Save the reviews info to local storage
                localStorage.setItem('reviewsList', JSON.stringify(reviews))

                return true
            } else {
                // Handle failure
                currentPostReviews.value = [{}]
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error);
        }
    }

    // GET Method to retrieve a specific Review:
    const getSingleReview = async (reviewId) => {
        try {

            const response = await getAPI.get(`/api/reviews/${reviewId}/get/`)

            if (response.data) {
                const postReviews = response.data

                currentPostReviews.value = postReviews

                // Save the reviews info to local storage
                localStorage.setItem('reviewsList', JSON.stringify(reviews))

                return true
            } else {
                // Handle failure
                currentPostReviews.value = [{}]
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error);
        }
    }

    // GET Method to retrieve all the User Reviews for a specific Post:
    const getUserReviewsForPost = async (postId, userId) => {

        try {

            const response = await getAPI.get(`/api/reviews/post/${postId}/user/${userId}/get/`)

            if (response.data) {
                const userReview = response.data

                userReviewsForPost.value = userReview

                // Save the user review info to local storage
                localStorage.setItem('userReview', JSON.stringify(userReviewsForPost))

                return true
            } else {
                // Handle failure
                userReviewsForPost.value = [{}]
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error);
        }
    }


    const postReview = async (review) => {
        try {
            const response = await getAPI.post('/api/reviews/post/', review, {
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${userInfo.value.token}`
            }
            });

            // Now we update the current post's reviews:
            getReviewsForPost()

            return true
        } catch (error) { 
            console.log(error);
            console.error(error);
            return false
        }
    }

    const updateReview = async (id, review) => {
        try {
            const response = await getAPI.put(`/api/reviews/${id}/update/`, review, {
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${userInfo.value.token}`
            }
            });

            // Now we update the current post's reviews:
            getReviewsForPost()

            return true
        } catch (error) { 
            console.log(error);
            console.error(error);
            return false
        }
    }

    const deleteReview = async (reviewId) => {
        try {
            const response = await getAPI.delete(`/api/reviews/${reviewId}/delete/`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${userInfo.value.token}`
                }
            })

            // Now we update the current post's reviews:
            getReviewsForPost()

            return true
        } catch (error) {
            console.log(error);
 
            return false
        }
    }



    return {getReviews, postReview, updateReview, deleteReview, 
        reviewsList, 
        getReviewsForPost, currentPostReviews, 
        getUserReviewsForPost, userReviewsForPost, 
        getSingleReview}
})
import { ref } from 'vue'
import { defineStore, storeToRefs } from 'pinia'
import { useUserLoggedStore } from './userLogged'
import { getAPI } from '../axios-api';

export const useReviewsStore = defineStore('reviewsStore', () => {

    const userLoggedStore = useUserLoggedStore()
    const { userInfo } = storeToRefs(userLoggedStore)

    const reviewsList = ref(null) 
    const currentPostReviews = ref(null)

    const userReviewsForPost = ref(null)

    const reviewId = ref(null)
    const postIdFromReview = ref(null)




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
                localStorage.setItem('reviewsList', JSON.stringify(postReviews))

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
                localStorage.setItem('reviewsList', JSON.stringify(postReviews))

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
    const getUserReviewsForPost = async (postId, userId, isUser) => {
        let response
        try {
            if (isUser) {
                // If there's a user logged in, check for the user's review for the postId
                response = await getAPI.get(`/api/reviews/post/${postId}/user/${userId}/get/`)
            } else if (userId) {
                // If there's not a user logged in, but we have a userId, it means that the anonymous_user is in the database
                // so we check with its userId for his review for the postId
                response = await getAPI.get(`/api/reviews/post/${postId}/anonymous_user/${userId}/get/`)
            }

            if (response.data) {
                const userReview = response.data[0]
                
                userReviewsForPost.value = userReview

                // Save the user review info to local storage
                localStorage.setItem('userReview', JSON.stringify(userReviewsForPost.value))

                return true
            } else {
                // There wasn't a user logged in nor an anon user saved in the database
                // Handle failure
                userReviewsForPost.value = [{}]
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error);
        }
    }


    const postReview = async (review, postId) => {
        try {
            const response = await getAPI.post('/api/reviews/post/', review, {
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${userInfo.value.token}`
            }
            });

            // Now we update the current post's reviews:
            getReviewsForPost(postId)

            return true
        } catch (error) { 
            console.log(error);
            console.error(error);
            return false
        }
    }

    const updateReview = async (id, review, user) => {

        if (user.anonymousIdentifier) {
            review.userInfo = { anonymousIdentifier: user.anonymousIdentifier}
        } else {
            review.userInfo = { id: user.id }
        }

        try {
            const response = await getAPI.put(`/api/reviews/${id}/update/`, review);

            // Now we update the current post's reviews:
            getReviewsForPost(review.post)

            return true
        } catch (error) { 
            console.log(error);
            console.error(error);
            return false
        }
    }

    const deleteReview = async (reviewId, postId, user) => {
        try {
            const response = await getAPI.delete(`/api/reviews/${reviewId}/delete/`, {
                data: {
                    userInfo: user
                }
            })

            // Now we update the current post's reviews:
            getReviewsForPost(postId)

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
        getSingleReview, reviewId}
})
import { ref } from 'vue'
import { defineStore, storeToRefs } from 'pinia'
import { useUserLoggedStore } from './userLogged'
import { getAPI } from '../axios-api';

export const useCommentsStore = defineStore('commentsStore', () => {

    const userLoggedStore = useUserLoggedStore()
    const { userInfo } = storeToRefs(userLoggedStore)

    const commentsList = ref(null) 
    const singleComment = ref(null) 
    const currentReviewComments = ref(null)
    const currentParentComments = ref(null)

    const userCommentsForReview = ref(null)
    const userCommentsForParent = ref(null)

    const commentId = ref(null)
    const reviewIdFromComment = ref(null)




    // GET Method to retrieve all the Reviews:
    const getComments = async () => {
        try {
            const response = await getAPI.get('/api/comments/get/')

            if(response.data) {
                const comments = response.data

                commentsList.value = comments
                // Save the comments info to local storage
                localStorage.setItem('commentsList', JSON.stringify(comments))

                return true
            } else {
                // Handle failure
                commentsList.value = [{}]
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error)
        }
    }

    // GET Method to retrieve all the Reviews for a specific Post:
    const getCommentsForReview = async (reviewId) => {

        try {

            const response = await getAPI.get(`/api/comments/review/${reviewId}/get/`)

            if (response.data) {
                const reviewComments = response.data

                currentReviewComments.value = reviewComments

                // Save the reviews info to local storage
                localStorage.setItem('commentsList', JSON.stringify(reviewComments))

                return true
            } else {
                // Handle failure
                currentReviewComments.value = null
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error);
        }
    }

    // GET Method to retrieve all the Comments for a specific Parent Comment:
    const getCommentsForParent = async (parentId) => {

        try {

            const response = await getAPI.get(`/api/comments/parent/${parentId}/get/`)

            if (response.data) {
                const parentComments = response.data

                currentParentComments.value = parentComments

                // Save the parents info to local storage
                localStorage.setItem('commentsList', JSON.stringify(parentComments))

                return true
            } else {
                // Handle failure
                currentParentComments.value = null
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error);
        }
    }

    // GET Method to retrieve a specific Review:
    const getSingleComment = async (commentId) => {
        try {

            const response = await getAPI.get(`/api/comments/${commentId}/get/`)

            if (response.data) {
                const comment = response.data

                singleComment.value = comment

                // Save the comment info to local storage
                localStorage.setItem('singleComment', JSON.stringify(comment))

                return true
            } else {
                // Handle failure
                singleComment.value = null
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error);
        }
    }

    // GET Method to retrieve all the User Reviews for a specific Post:
    const getUserCommentsForReview = async (reviewId, userId, isUser) => {
        let response
        try {
            if (isUser) {
                // If there's a user logged in, check for the user's review for the postId
                response = await getAPI.get(`/api/comments/review/${reviewId}/user/${userId}/get/`)
            } else if (userId) {
                // If there's not a user logged in, but we have a userId, it means that the anonymous_user is in the database
                // so we check with its userId for his review for the postId
                response = await getAPI.get(`/api/comments/review/${reviewId}/anonymous_user/${userId}/get/`)
            }

            if (response.data[0]) {
                const userComments = response.data[0]
 
                userCommentsForReview.value = userComments

                return true
            } else {
                // There wasn't a user logged in nor an anon user saved in the database
                // Handle failure
                userCommentsForReview.value = null
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error);
        }
    }

    // GET Method to retrieve all the User Comments for a specific Parent Comment:
    const getUserCommentsForParent = async (parentId, userId, isUser) => {
        let response
        try {
            if (isUser) {
                // If there's a user logged in, check for the user's comments for the parentId
                response = await getAPI.get(`/api/comments/parent/${parentId}/user/${userId}/get/`)
            } else if (userId) {
                // If there's not a user logged in, but we have a userId, it means that the anonymous_user is in the database
                // so we check with its userId for his comments for the parentId
                response = await getAPI.get(`/api/comments/parent/${parentId}/anonymous_user/${userId}/get/`)
            }

            if (response.data[0]) {
                const userComments = response.data[0]
 
                userCommentsForParent.value = userComments

                return true
            } else {
                // There wasn't a user logged in nor an anon user saved in the database
                // Handle failure
                userCommentsForParent.value = null
                // Throw an error or display an error message to the user
                return false
            }

        } catch (error) {
            console.log(error);
        }
    }


    const postComment = async (comment, reviewId) => {
        try {
            const response = await getAPI.post('/api/comments/post/', comment, {
            headers: {
                'Content-Type': 'application/json',
            }
            });

            // Now we update the current post's comments:
            await getCommentsForReview(reviewId)

            return true
        } catch (error) { 
            console.log(error);
            console.error(error);
            return false
        }
    }

    const updateComment = async (id, comment, user) => {

        if (user.anonymous_identifier) {
            comment.userInfo = { anonymous_identifier: user.anonymous_identifier}
        } else {
            comment.userInfo = { id: user.id }
        }

        try {
            const response = await getAPI.put(`/api/comments/${id}/update/`, comment);

            // Now we update the current post's reviews:
            getCommentsForReview(comment.review)

            return true
        } catch (error) { 
            console.log(error);
            console.error(error);
            return false
        }
    }

    const deleteComment = async (commentId, reviewId, user) => {
        try {
            const response = await getAPI.delete(`/api/comments/${commentId}/delete/`, {
                data: {
                    userInfo: user
                }
            })

            // Now we update the current post's reviews:
            getCommentsForReview(reviewId)

            return true
        } catch (error) {
            console.log(error);
 
            return false
        }
    }



    return {getComments, postComment, updateComment, deleteComment, 
        commentsList, 
        getCommentsForReview, currentReviewComments, 
        getCommentsForParent, currentParentComments,
        getUserCommentsForReview, userCommentsForReview, 
        getSingleComment, commentId}
})
<template>
    <div v-if="isOpen" class="comments-thread-container">
        <h1 class="review__title">- Comments ({{countComments}}) -</h1>
        <div class="reviews-container comments-container">
            <LeaveComment :reviewId="parentId" />
            <ReviewComment 
                v-for="comment in thisReviewComments.filter(comment => comment.review === parentId)" :key="comment.id" 
                class="comment" 
                :comment="comment" 
                ref="childComponentRef"    
            />
        </div>
    </div>
    <AreYouSureModal 
        :action="'delete'"
        :method="handleDeleteComment"
    />
</template>


<script setup>
import { defineProps } from 'vue';
import { storeToRefs } from 'pinia';
import { useCommentsStore } from '../../stores/comments';
import { useUserLoggedStore } from '../../stores/userLogged';
import ReviewComment from './ReviewComment.vue';
import LeaveComment from './LeaveComment.vue';


import AreYouSureModal from '../Elements/AreYouSureModal.vue';



const props = defineProps({
    parentId: {
        type: Number,
        required: true
    },
    parent: String,
    isOpen: Boolean
})

const commentsStore = useCommentsStore()
const { getCommentsForReview, deleteComment } = commentsStore
const { currentReviewComments, commentId } = storeToRefs(commentsStore)

const userLoggedStore = useUserLoggedStore()
const { userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)


await getCommentsForReview(Number(props.parentId))
const countComments = currentReviewComments.value.length


const thisReviewComments = currentReviewComments.value
const handleDeleteComment = async () => {
    if (userInfo.value) {
        await deleteComment(commentId.value, Number(props.parentId), userInfo.value)
    } else if (anonymousUserInfo.value) {
        await deleteComment(commentId.value, Number(props.parentId), anonymousUserInfo.value)
    }
    reviewId.value = null
}

</script>
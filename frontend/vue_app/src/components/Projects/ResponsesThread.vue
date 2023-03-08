<template>
    <div v-if="isOpen" class="comments-thread-container">
        <h1 class="review__title">- Comments ({{countComments}}) -</h1>
        <div class="reviews-container comments-container">
            <LeaveComment :reviewId="parentId" />
            <ReviewComment 
                v-for="comment in thisParentComments.filter(comment => comment.parent === parentId)" :key="comment.id" 
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
const { getCommentsForParent, deleteComment } = commentsStore
const { currentParentComments, commentId } = storeToRefs(commentsStore)

const userLoggedStore = useUserLoggedStore()
const { userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)


await getCommentsForParent(Number(props.parentId))
const countComments = currentParentComments.value.length


const thisParentComments = currentParentComments.value
const handleDeleteComment = async () => {
    if (userInfo.value) {
        await deleteComment(commentId.value, Number(props.parentId), userInfo.value)
    } else if (anonymousUserInfo.value) {
        await deleteComment(commentId.value, Number(props.parentId), anonymousUserInfo.value)
    }
    parentId.value = null
}

</script>
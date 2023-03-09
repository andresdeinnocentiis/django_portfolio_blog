<template>
    <div>
        <h1 v-if="isOpen"  class="review__title">- Replies ({{countComments}}) -</h1>
        <transition 
            enter-active-class="animate__animated animate__bounceIn"
            leave-active-class="animate__animated animate__bounceOut"
            mode="out-in" 
        >
            <div v-if="isOpen" class="comments-thread-container">
                
                <div class="reviews-container comments-container">
                    <!--<LeaveComment :reviewId="parentId" />-->
                    <CommentResponse 
                        v-for="response in thisParentComments.filter(response => response.parent === parentId)" :key="response.id" 
                        class="comment" 
                        :response="response"    
                    />
                </div>
            </div>
        </transition>
        <AreYouSureModal 
            :action="'delete'"
            :method="handleDeleteComment"
        />
    </div>
</template>


<script setup>
import { defineProps } from 'vue';
import { storeToRefs } from 'pinia';
import { useCommentsStore } from '../../stores/comments';
import { useUserLoggedStore } from '../../stores/userLogged';
import CommentResponse from './CommentResponse.vue';
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
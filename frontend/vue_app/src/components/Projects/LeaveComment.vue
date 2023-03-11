<template>
    <div class="leave-review-container leave-comment-container">
        <div class="leave-review-write">
            <div class="review-header">
                <div v-if="userInfo" class="user-verified-container">
                    <div class="user-verified-img">
                        <img v-if="userInfo.image" :src="userInfo.image" alt="">
                        <font-awesome-icon icon="fa-solid fa-user" v-else />
                    </div>
                    <div class="user-date">
                        <div class="user-verified-data">
                            <p class="review-username">{{userInfo.username}}</p>
                            <font-awesome-icon icon="fa-solid fa-circle-check" />
                        </div>
                    </div>
                </div>

                <div v-else-if="anonymousUserInfo" class="user-verified-container">
                    <div class="user-date">
                        <div v-if="anonymousUserInfo.username" class="user-verified-data">
                            <p class="review-username">{{anonymousUserInfo.username}}</p>
                        </div>
                        <label v-else class="custom-field field-review" aria-label="Enter username">
                            <input v-model="newComment.username" type="text" required placeholder="&nbsp;"/>
                            <span class="placeholder">Enter Username</span>
                        </label>
                    </div>
                </div>
            </div>
            <label class="custom-field" aria-label="Enter review">
                <textarea style="resize: none;" class="review-edit newReview" autofocus v-model="newComment.content" type="text" required placeholder="&nbsp;" rows="4" cols="50" />
                <span class="placeholder-textarea">Comment the review here!</span>
            </label>
            
            <div class="review-extra-container confirm-edit-container">
                <font-awesome-icon icon="fa-solid fa-check" class="review-icon-confirm" @click.prevent="handleConfirmNewComment" />
                <font-awesome-icon icon="fa-solid fa-xmark" class="review-icon-cancel" @click.prevent="cancelLeaveComment" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, watchEffect, defineEmits, watch } from 'vue';
import { storeToRefs } from 'pinia';
import { useUserLoggedStore } from "../../stores/userLogged";
import { useCommentsStore } from '../../stores/comments';


const userLoggedStore = useUserLoggedStore()
const { userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)
const { createAnonymousUser } = userLoggedStore

const commentsStore = useCommentsStore()
const { postComment, getComments} = commentsStore
const { currentReviewComments } = storeToRefs(commentsStore)

const props = defineProps({
    reviewId: {
        type: Number
    },
    parentId: {
        type: Number
    },
    parent: String
})

const leaveComment = ref(false)



// I define the emit event for updating this value and passing it up to its parent component
const emits = defineEmits(["update:onLeaveComment","new-comment"]);


const newComment = ref({
    username: userInfo.value ? userInfo.value.username : anonymousUserInfo.value.username ? anonymousUserInfo.value.username : "",
    content: "",
    rating: 0
})

const cancelLeaveComment = () => {
    newComment.value.username = userInfo.value && userInfo.value.username ? userInfo.value.username : anonymousUserInfo.value && anonymousUserInfo.value.username ? anonymousUserInfo.value.username : "" 
    newComment.value.content = "" 

    emits("update:onLeaveComment", leaveComment.value)
}

const handleConfirmNewComment = async () => {
    
    if (anonymousUserInfo.value && anonymousUserInfo.value.id) {
        // if it's an anon user and is already on the database:
        const commentObj = {
            review: props.parent == "review" ? props.reviewId : null,
            user: null,
            anonymous_user: anonymousUserInfo.value.id,
            content: newComment.value.content,
            parent: props.parent == "comment" ? props.parentId : null
        }
        try {
            await postComment(commentObj)
            emits("new-comment")
            emits("update:onLeaveComment", leaveComment.value)

        } catch(error) {
            console.log(error);
        }

    } else if (userInfo.value) {
        // If it's a registered user:
        const commentObj = {
            review:  props.parent == "review" ? props.reviewId : null,
            user: userInfo.value.id,
            anonymous_user: null,
            content: newComment.value.content,
            parent: props.parent == "comment" ? props.parentId : null
        }

        try {
            await postComment(commentObj)
            emits("new-comment")
            emits("update:onLeaveComment", leaveComment.value)
        } catch(error) {
            console.log(error);
        }
        
    } else {
        // If it's an anon user and is not yet on the database

        const newAnonUser = {
            username: newComment.value.username,
            anonymous_identifier: anonymousUserInfo.value.anonymous_identifier
        }
        const success = await createAnonymousUser(newAnonUser)
        if (success) {

            const commentObj = {
                review: props.parent == "review" ? props.reviewId : null,
                user: null,
                anonymous_user: anonymousUserInfo.value.id,
                content: newComment.value.content,
                parent: props.parent == "comment" ? props.parentId : null
            }

            try {
                await postComment(commentObj)
                emits("new-comment")
                emits("update:onLeaveComment", leaveComment.value)
            } catch(error) {
                console.log(error);
            }

            
        }
    }

    emits("update:onLeaveComment", leaveComment.value)

    await userLeftComment()
    
}


const userLeftComment = async () => {
    getComments()
}

await userLeftComment()

onMounted(async () => {

  await userLeftComment()

})

watchEffect(async () => {
    currentReviewComments.value
    await userLeftComment()
})

</script>
<template>
    <div>
    
        <div class="review comment-container response-container"
            :class="{'comment-isOwner':response.user && userInfo && response.user.id === userInfo.id || response.anonymous_user && anonymousUserInfo && response.anonymous_user.id === anonymousUserInfo.id}"
        >
            <div class="review-header">
                
                <div v-if="response.user" class="user-verified-container">
                    <div class="user-verified-img">
                        <img v-if="response.user.image" :src="response.user.image" alt="">
                        <font-awesome-icon icon="fa-solid fa-user" v-else />
                    </div>
                    <div class="user-date">
                        <div class="user-verified-data">
                            <a v-if="response.user.linkedin" :href="response.user.linkedin" target="_blank" class="review-username comment-username">{{response.user.username}}</a>
                            <p v-else class="review-username comment-username">{{response.user.username}}</p>
                            <font-awesome-icon icon="fa-solid fa-circle-check" />
                        </div>
                        <p class="review-datetime">{{ formattedDate }}</p>
                    </div>
                </div>
                <div v-else class="user-verified-container">
                    <div class="user-verified-img">
                        <font-awesome-icon icon="fa-solid fa-user" />
                    </div>
                    <div class="user-date">
                        <div class="user-verified-data">
                            <p class="review-username comment-username">{{response.anonymous_user ? response.anonymous_user.username : "" }}</p>
                        </div>
                        <p class="review-datetime">{{ formattedDate }}</p>
                    </div>
                </div>
            </div>
            <label v-if="onEdit" class="custom-field" aria-label="Enter comment"
            :class="{'placeholder-isOwner':response.user && userInfo && response.user.id === userInfo.id || response.anonymous_user && anonymousUserInfo && response.anonymous_user.id === anonymousUserInfo.id}"
            >
                <textarea style="resize: none;" class="review-edit" autofocus v-model="response.content" type="text" required placeholder="&nbsp;" rows="4" cols="50">
                {{response.content}}
                </textarea>
                <span class="placeholder-textarea">Write your reply</span>
            </label>
            <p v-else class="review-content"><strong>@{{repliedTo}}</strong>, {{response.content}}</p>
            
            <div v-if="onEdit" class="review-extra-container confirm-edit-container comment-extra-container"
                :class="{'comment-extra-isOwner':response.user && userInfo && response.user.id === userInfo.id || response.anonymous_user && anonymousUserInfo && response.anonymous_user.id === anonymousUserInfo.id}"
            >
                <font-awesome-icon icon="fa-solid fa-check" class="review-icon-confirm" @click.prevent="handleConfirmEdit" />
                <font-awesome-icon icon="fa-solid fa-xmark" class="review-icon-cancel" @click.prevent="cancelEditResponse" />
            </div>
            <div v-else class="review-extra-container comment-extra-container"
            :class="{'comment-extra-isOwner':response.user && userInfo && response.user.id === userInfo.id || response.anonymous_user && anonymousUserInfo && response.anonymous_user.id === anonymousUserInfo.id}"
            >
                <div class="review__icons-div comment__icons-div" 
                :class="{'icons-div-isOwner':response.user && userInfo && response.user.id === userInfo.id || response.anonymous_user && anonymousUserInfo && response.anonymous_user.id === anonymousUserInfo.id}"
                >
                    <div class="like-action-container"  @click.prevent="handleCommentLikeClick(response.id)">
                        <font-awesome-icon class="review-icons icons__like-action" v-if="isLiked" icon="fa-solid fa-heart" />
                        <font-awesome-icon class="review-icons icons__like-action" v-else icon="fa-regular fa-heart" />
                    </div>
                    <font-awesome-icon class="review-icons icons__comment-action" icon="fa-regular fa-comment" @click.prevent="toggleLeaveResponse" />
                </div>
                <div class="likes-count">
                    <p class="count-text"><span class="amount-likes">{{ response.likes }}</span> {{ response.likes != 1 ? 'likes' : 'like' }}</p>
                    <div class="comments-action"  @click.prevent="toggleShowResponses">
                        <p class="count-text count-comments"><span class="amount-likes">{{ response.comments }}</span> {{ response.comments != 1 ? 'replies' : 'reply' }}</p>
                        <font-awesome-icon v-if="response.comments && !showResponses" icon="fa-solid fa-angle-down" />
                        <font-awesome-icon v-if="showResponses" icon="fa-solid fa-angle-up" />
                    </div>
                </div>
                <div v-if="userInfo && isUserAdmin || isUserOwner" class="review-admin-actions-container comment-admin-actions-container"
                    :class="{'admin-actions-isOwner':response.user && userInfo && response.user.id === userInfo.id || response.anonymous_user && anonymousUserInfo && response.anonymous_user.id === anonymousUserInfo.id}"
                >
                    <font-awesome-icon v-if="isUserOwner" icon="fa-solid fa-pen-to-square" class="review-admin-action-btn edit" @click.prevent="toggleEditComment"/>
                    <font-awesome-icon icon="fa-solid fa-trash" class="review-admin-action-btn delete" @click.prevent="handleDeleteResponse" />
                </div>
            </div>
        </div>
        <LeaveComment 
            v-if="onLeaveResponse" 
            :parentId="response.id" 
            :parent="'comment'"
            @update:onLeaveComment="closeLeaveResponse" 
            @new-comment="handleNewResponse" 
        /> 

        <div v-if="response.comments > 0 && showResponses">
            <h1 v-if="showResponses" class="review__title">- Replies -</h1>
            <transition 
                enter-active-class="animate__animated animate__bounceIn"
                leave-active-class="animate__animated animate__bounceOut"
                mode="out-in" 
            >
                <div v-if="showResponses" class="comments-thread-container">
                    
                    <div class="reviews-container comments-container">
                        <!--<LeaveComment :reviewId="parentId" />-->
                        <CommentResponse 
                            v-for="response in thisParentComments.value" 
                            :key="response.id" 
                            class="comment" 
                            :response="response"    
                        />
                    </div>
                </div>
            </transition>
        </div>
    </div>
</template>

<script setup>
import { watchEffect, ref, defineEmits, onMounted, computed } from "vue";
import { storeToRefs } from "pinia";
import { useCommentsStore } from "../../stores/comments";
import { useUserLoggedStore } from "../../stores/userLogged";
import { useLikesStore } from "../../stores/likes";
import { useModalStore } from "../../stores/modal";
import LeaveComment from "./LeaveComment.vue";



const props = defineProps({
    response: {
        type: Object,
        required: true
    },
    id: Number,
    repliedTo: String
})

const responseContent = props.response.content
const onEdit = ref(false)

const onLeaveResponse = ref(false)

const emits = defineEmits(['delete-comment'])

const userLoggedStore = useUserLoggedStore()
const { isUserAdmin, userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)

const commentsStore = useCommentsStore()
const { updateResponse, getComments, deleteComment} = commentsStore
const { commentId, commentsList } = storeToRefs(commentsStore)

const likesStore = useLikesStore()
const { postLike, deleteLike, getUserLikeForComment } = likesStore
const { currentCommentLike, isCommentLikedByUser } = storeToRefs(likesStore)

const modalStore = useModalStore()
const { toggleSureModal } = modalStore


const isLiked = ref(false)

const showResponses = ref(false)

await getComments()
let thisParentComments = ref([])

let isUserOwner 

if (userInfo.value) {
    isUserOwner = props.response.user && props.response.user.id == userInfo.value.id  ? true : false
} else if (anonymousUserInfo.value) {
    isUserOwner = props.response.anonymous_user && props.response.anonymous_user.anonymous_identifier == anonymousUserInfo.value.anonymous_identifier ? true : false
} else {
    isUserOwner = false
}

const toggleEditComment = () => {  
    onEdit.value = !onEdit.value
}

const toggleShowResponses = () => {
    showResponses.value = !showResponses.value
}

const cancelEditResponse = () => {
    // If the user made some modifications but didn't want to save the edit, we set the content back to its original value 
    props.response.content = responseContent
    onEdit.value = false
}


const handleDeleteResponse = async () => {
    commentId.value = props.response.id
    if (userInfo.value) {
        await deleteComment(commentId.value, userInfo.value)
    } else if (anonymousUserInfo.value) {
        await deleteComment(commentId.value, anonymousUserInfo.value)
    }
    commentId.value = null
    emits("delete-comment")
    await getComments()
}

const handleCommentLikeClick = async (commentId) => {

    // Create the Like Object that would be sent if the request is POST
    const likeObj = {
        user: userInfo.value ? userInfo.value.id : null,
        anonymous_identifier: anonymousUserInfo.value ? anonymousUserInfo.value.anonymous_identifier : null,
        comment: commentId 
    }
    // If it's a logged user:
    if(userInfo.value) {
        await getUserLikeForComment(commentId, userInfo.value)
        try {
            // If the comment is already liked and the user clicked it, then it has to be deleted
            if (isCommentLikedByUser.value) {
                await deleteLike(currentCommentLike.value.id)
                // Update the like to see the changes in real time
                await getUserLikeForComment(commentId, userInfo.value)
                isLiked.value = false
                props.response.likes--
    
            // If the comment is not yet liked and the user clicked it, then it has to be created
            } else {
                await postLike(likeObj)
                // Update the like to see the changes in real time
                await getUserLikeForComment(commentId, userInfo.value)
                isLiked.value = true
                props.response.likes++
            }
        } catch(error) {
            console.error(error);
        }
    // If it's an unregistered user:    
    } else {
        await getUserLikeForComment(commentId, anonymousUserInfo.value)
        try {
            // If the comment is already liked and the user clicked it, then it has to be deleted
            if (isCommentLikedByUser.value) {
                await deleteLike(currentCommentLike.value.id)
                // Update the like to see the changes in real time
                await getUserLikeForComment(commentId, anonymousUserInfo.value)
                isLiked.value = false
                props.response.likes--
            // If the comment is not yet liked and the user clicked it, then it has to be created
            } else {
                await postLike(likeObj)
                // Update the like to see the changes in real time
                await getUserLikeForComment(commentId, anonymousUserInfo.value)
                isLiked.value = true
                props.response.likes++
            } 
        } catch(error) {
            console.error(error);
        }
        
    }

}



const toggleLeaveResponse = () => {
    onLeaveResponse.value = !onLeaveResponse.value
}

const closeLeaveResponse = () => {
    onLeaveResponse.value = false
}


const handleNewResponse = () => {
    props.response.comments += 1 
}

const handleConfirmEdit = async () => {
    commentId.value = props.response.id
    try {
        if (userInfo.value) {
        await updateResponse(commentId.value, props.response, userInfo.value)
    } else if (anonymousUserInfo.value) {
        await updateResponse(commentId.value, props.response, anonymousUserInfo.value)
    }

    } catch(error) {
            console.error(error);
    }

    //getPostDetails(props.response.post) Need to get the post Id from somewhere

    onEdit.value = false
}


if (userInfo.value) {
    await getUserLikeForComment(props.response.id, userInfo.value)
    isLiked.value = isCommentLikedByUser.value

} else {
    await getUserLikeForComment(props.response.id, anonymousUserInfo.value)
    isLiked.value = isCommentLikedByUser.value
}

const date = new Date(props.response.created_at);
const options = {
  day: "2-digit",
  month: "2-digit",
  year: "numeric",
  hour: "numeric",
  minute: "2-digit",
  hour12: true
};
const formattedDate = date.toLocaleDateString("en-US", options).replace('AM', 'a.m.').replace('PM', 'p.m.');



onMounted(async () => {
    await getComments();
    
    thisParentComments.value = computed(() => commentsList.value.filter((comment) => comment.parent === props.response.id))
});

watchEffect(async() => {

    await getComments()
    thisParentComments.value = computed(() => commentsList.value.filter((comment) => comment.parent === props.response.id))

})

</script>
<template>
    <div>

        <div class="review comment-container"
            :class="{'comment-isOwner':comment.user && userInfo && comment.user.id === userInfo.id || comment.anonymous_user && anonymousUserInfo && comment.anonymous_user.id === anonymousUserInfo.id}"
        >
            <div class="review-header">
                
                <div v-if="comment.user" class="user-verified-container">
                    <div class="user-verified-img">
                        <img v-if="comment.user.image" :src="comment.user.image" alt="">
                        <font-awesome-icon icon="fa-solid fa-user" v-else />
                    </div>
                    <div class="user-date">
                        <div class="user-verified-data">
                            <a v-if="comment.user.linkedin" :href="comment.user.linkedin" target="_blank" class="review-username comment-username">{{comment.user.username}}</a>
                            <p v-else class="review-username comment-username">{{comment.user.username}}</p>
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
                            <p class="review-username comment-username">{{comment.anonymous_user ? comment.anonymous_user.username : "" }}</p>
                        </div>
                        <p class="review-datetime">{{ formattedDate }}</p>
                    </div>
                </div>
            </div>
            <label v-if="onEdit" class="custom-field" aria-label="Enter comment">
                <textarea style="resize: none;" class="review-edit" autofocus v-model="comment.content" type="text" required placeholder="&nbsp;" rows="4" cols="50">
                {{comment.content}}
                </textarea>
                <span class="placeholder-textarea">Write your comment</span>
            </label>
            <p v-else class="review-content"><strong>@{{repliedTo}}</strong>, {{comment.content}}</p>
            
            <div v-if="onEdit" class="review-extra-container confirm-edit-container comment-extra-container"
                :class="{'comment-extra-isOwner':comment.user && userInfo && comment.user.id === userInfo.id || comment.anonymous_user && anonymousUserInfo && comment.anonymous_user.id === anonymousUserInfo.id}"
            >
                <font-awesome-icon icon="fa-solid fa-check" class="review-icon-confirm" @click.prevent="handleConfirmEdit" />
                <font-awesome-icon icon="fa-solid fa-xmark" class="review-icon-cancel" @click.prevent="cancelEditComment" />
            </div>
            <div v-else class="review-extra-container comment-extra-container"
            :class="{'comment-extra-isOwner':comment.user && userInfo && comment.user.id === userInfo.id || comment.anonymous_user && anonymousUserInfo && comment.anonymous_user.id === anonymousUserInfo.id}"
            >
                <div class="review__icons-div comment__icons-div" 
                :class="{'icons-div-isOwner':comment.user && userInfo && comment.user.id === userInfo.id || comment.anonymous_user && anonymousUserInfo && comment.anonymous_user.id === anonymousUserInfo.id}"
                >
                    <div class="like-action-container"  @click.prevent="handleCommentLikeClick(comment.id)">
                        <font-awesome-icon class="review-icons icons__like-action" v-if="isLiked" icon="fa-solid fa-heart" />
                        <font-awesome-icon class="review-icons icons__like-action" v-else icon="fa-regular fa-heart" />
                    </div>
                    <font-awesome-icon class="review-icons icons__comment-action" icon="fa-regular fa-comment" @click.prevent="toggleLeaveComment" />
                </div>
                <div class="likes-count">
                    <p class="count-text"><span class="amount-likes">{{ comment.likes }}</span> {{ comment.likes != 1 ? 'likes' : 'like' }}</p>
                    <div class="comments-action"  @click.prevent="toggleShowResponses">
                        <p class="count-text count-comments"><span class="amount-likes">{{ comment.comments }}</span> {{ comment.comments != 1 ? 'replies' : 'reply' }}</p>
                        <font-awesome-icon v-if="comment.comments && !showResponses" icon="fa-solid fa-angle-down" />
                        <font-awesome-icon v-if="showResponses" icon="fa-solid fa-angle-up" />
                    </div>
                </div>
                <div v-if="userInfo && isUserAdmin || isUserOwner" class="review-admin-actions-container comment-admin-actions-container"
                    :class="{'admin-actions-isOwner':comment.user && userInfo && comment.user.id === userInfo.id || comment.anonymous_user && anonymousUserInfo && comment.anonymous_user.id === anonymousUserInfo.id}"
                >
                    <font-awesome-icon v-if="isUserOwner" icon="fa-solid fa-pen-to-square" class="review-admin-action-btn edit" @click.prevent="toggleEditComment"/>
                    <font-awesome-icon icon="fa-solid fa-trash" class="review-admin-action-btn delete" @click.prevent="handleDeleteComment" />
                </div>
            </div>
        </div>
        <LeaveComment 
            v-if="onLeaveComment" 
            :parentId="comment.id" 
            :parent="'comment'"
            @update:onLeaveComment="closeLeaveComment" 
            @new-comment="handleNewResponse" 
        /> 

        <div v-if="comment.comments > 0 && showResponses">
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
                            :repliedTo="comment.user ? comment.user.username : comment.anonymous_user.username"
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
import CommentResponse from "./CommentResponse.vue";



const props = defineProps({
    comment: {
        type: Object,
        required: true
    },
    id: Number,
    repliedTo: String
})

const commentContent = props.comment.content
const onEdit = ref(false)

const onLeaveComment = ref(false)

const emits = defineEmits(['delete-comment'])

const userLoggedStore = useUserLoggedStore()
const { isUserAdmin, userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)

const commentsStore = useCommentsStore()
const { updateComment, getComments, deleteComment} = commentsStore
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
    isUserOwner = props.comment.user && props.comment.user.id == userInfo.value.id  ? true : false
} else if (anonymousUserInfo.value) {
    isUserOwner = props.comment.anonymous_user && props.comment.anonymous_user.anonymous_identifier == anonymousUserInfo.value.anonymous_identifier ? true : false
} else {
    isUserOwner = false
}

const toggleEditComment = () => {  
    onEdit.value = !onEdit.value
}

const toggleShowResponses = () => {
    showResponses.value = !showResponses.value
}


const closeLeaveComment = () => {
    onLeaveComment.value = false
}

const cancelEditComment = () => {
    // If the user made some modifications but didn't want to save the edit, we set the content back to its original value 
    props.comment.content = commentContent
    onEdit.value = false
}

const toggleLeaveComment = () => {
    onLeaveComment.value = !onLeaveComment.value
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
                props.comment.likes--
    
            // If the comment is not yet liked and the user clicked it, then it has to be created
            } else {
                await postLike(likeObj)
                // Update the like to see the changes in real time
                await getUserLikeForComment(commentId, userInfo.value)
                isLiked.value = true
                props.comment.likes++
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
                props.comment.likes--
            // If the comment is not yet liked and the user clicked it, then it has to be created
            } else {
                await postLike(likeObj)
                // Update the like to see the changes in real time
                await getUserLikeForComment(commentId, anonymousUserInfo.value)
                isLiked.value = true
                props.comment.likes++
            } 
        } catch(error) {
            console.error(error);
        }
        
    }

}


const handleConfirmEdit = async () => {
    commentId.value = props.comment.id
    try {
        if (userInfo.value) {
        await updateComment(commentId.value, props.comment, userInfo.value)
    } else if (anonymousUserInfo.value) {
        await updateComment(commentId.value, props.comment, anonymousUserInfo.value)
    }

    } catch(error) {
            console.error(error);
    }

    //getPostDetails(props.comment.post) Need to get the post Id from somewhere

    onEdit.value = false
}


if (userInfo.value) {
    await getUserLikeForComment(props.comment.id, userInfo.value)
    isLiked.value = isCommentLikedByUser.value

} else {
    await getUserLikeForComment(props.comment.id, anonymousUserInfo.value)
    isLiked.value = isCommentLikedByUser.value
}

const date = new Date(props.comment.created_at);
const options = {
  day: "2-digit",
  month: "2-digit",
  year: "numeric",
  hour: "numeric",
  minute: "2-digit",
  hour12: true
};
const formattedDate = date.toLocaleDateString("en-US", options).replace('AM', 'a.m.').replace('PM', 'p.m.');



const handleNewResponse = () => {
    props.comment.comments += 1 
}



const handleDeleteComment = async () => {
    commentId.value = props.comment.id
    if (userInfo.value) {
        await deleteComment(commentId.value, userInfo.value)
    } else if (anonymousUserInfo.value) {
        await deleteComment(commentId.value, anonymousUserInfo.value)
    }
    commentId.value = null
    emits("delete-comment")
    await getComments()
}

onMounted(async () => {
    await getComments();
    
    thisParentComments.value = computed(() => commentsList.value.filter((comment) => comment.parent === props.comment.id))
});

watchEffect(async() => {

    await getComments()
    thisParentComments.value = computed(() => commentsList.value.filter((comment) => comment.parent === props.comment.id))

})
</script>
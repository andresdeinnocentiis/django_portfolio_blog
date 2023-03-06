<template>
    <div>
        <div class="review-header">
            
            <div v-if="review.user" class="user-verified-container">
                <div class="user-verified-img">
                    <img v-if="review.user.image" :src="review.user.image" alt="">
                    <font-awesome-icon icon="fa-solid fa-user" v-else />
                </div>
                <div class="user-date">
                    <div class="user-verified-data">
                        <a v-if="review.user.linkedin" :href="review.user.linkedin" target="_blank" class="review-username">{{review.user.username}}</a>
                        <p v-else class="review-username">{{review.user.username}}</p>
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
                        <p class="review-username">{{review.anonymous_user.username}}</p>
                    </div>
                    <p class="review-datetime">{{ formattedDate }}</p>
                </div>
            </div>
            <StarRatingAction color="#27D49F" v-if="onEdit" class="edit-rating" v-model="review.rating" @update:value="handleUpdateValue" />
            <StarRating v-else :color="'#27D49F'" :value="review.rating" :className="'single-review'"/>
        </div>
        <label v-if="onEdit" class="custom-field" aria-label="Enter review">
            <textarea style="resize: none;" class="review-edit" autofocus v-model="review.content" type="text" required placeholder="&nbsp;" rows="4" cols="50">
            {{review.content}}
            </textarea>
            <span class="placeholder-textarea">Write your review</span>
        </label>
        <p v-else class="review-content">{{review.content}}</p>
        
        <div v-if="onEdit" class="review-extra-container confirm-edit-container">
            <font-awesome-icon icon="fa-solid fa-check" class="review-icon-confirm" @click.prevent="handleConfirmEdit" />
            <font-awesome-icon icon="fa-solid fa-xmark" class="review-icon-cancel" @click.prevent="cancelEditReview" />
        </div>
        <div v-else class="review-extra-container">
            <div class="review__icons-div" >
                <div class="like-action-container"  @click.prevent="handleReviewLikeClick(review.id)">
                    <font-awesome-icon class="review-icons icons__like-action" v-if="isLiked" icon="fa-solid fa-heart" />
                    <font-awesome-icon class="review-icons icons__like-action" v-else icon="fa-regular fa-heart" />
                </div>
                <font-awesome-icon class="review-icons icons__comment-action" icon="fa-regular fa-comment" />
            </div>
            <div class="likes-count">
                <p class="count-text"><span class="amount-likes">{{ review.likes }}</span> {{ review.likes != 1 ? 'likes' : 'like' }}</p>
                <div class="comments-action">
                    <p class="count-text count-comments"><span class="amount-likes">{{ review.comments }}</span> {{ review.comments != 1 ? 'comments' : 'comment' }}</p>
                    <font-awesome-icon v-if="review.comments" icon="fa-solid fa-angle-down" />
                </div>
            </div>
            <div v-if="userInfo && isUserAdmin || isUserOwner" class="review-admin-actions-container">
                <font-awesome-icon v-if="isUserOwner" icon="fa-solid fa-pen-to-square" class="review-admin-action-btn edit" @click.prevent="toggleEditReview"/>
                <font-awesome-icon icon="fa-solid fa-trash" class="review-admin-action-btn delete" @click.prevent="handleToggleSureModal" />
            </div>
        </div>
        
    </div>

    
    
</template>

<script setup>
import { readonly, ref, defineEmits } from "vue";
import { storeToRefs } from "pinia";
import { useReviewsStore } from "../../stores/reviews";
import { useUserLoggedStore } from "../../stores/userLogged";
import { useLikesStore } from "../../stores/likes";
import { useModalStore } from "../../stores/modal";
import { usePostsStore } from "../../stores/posts";
import StarRating from '../Elements/StarRating.vue';
import StarRatingAction from "../Elements/StarRatingAction.vue";



const props = defineProps({
    review: {
        type: Object,
        required: true
    }
})

const reviewContent = props.review.content
const realUserRating = props.review.rating
const onEdit = ref(false)

const emits = defineEmits(['delete-review'])

const userLoggedStore = useUserLoggedStore()
const { isUserAdmin, userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)

const reviewsStore = useReviewsStore()
const { updateReview} = reviewsStore
const { reviewId } = storeToRefs(reviewsStore)

const likesStore = useLikesStore()
const { postLike, deleteLike, getUserLikeForReview } = likesStore
const { currentReviewLike, isReviewLikedByUser } = storeToRefs(likesStore)

const modalStore = useModalStore()
const { toggleSureModal } = modalStore

const postsStore = usePostsStore()
const { getPostDetails } = postsStore


const isLiked = ref(false)


let isUserOwner 

if (userInfo.value) {
    isUserOwner = props.review.user && props.review.user.id == userInfo.value.id  ? true : false
} else if (anonymousUserInfo.value) {
    isUserOwner = props.review.anonymous_user && props.review.anonymous_user.anonymous_identifier == anonymousUserInfo.value.anonymousIdentifier ? true : false
} else {
    isUserOwner = false
}

const toggleEditReview = () => {  
    onEdit.value = !onEdit.value
}

const cancelEditReview = () => {
    // If the user made some modifications but didn't want to save the edit, we set the content back to its original value 
    props.review.content = reviewContent
    props.review.rating = realUserRating
    onEdit.value = false
}


// Function to get the value from the child component StarRatingAction
const handleUpdateValue = (value) => {
    props.review.rating = value
}


const handleReviewLikeClick = async (reviewId) => {

    // Create the Like Object that would be sent if the request is POST
    const likeObj = {
        user: userInfo.value ? userInfo.value.id : null,
        anonymous_identifier: anonymousUserInfo.value ? anonymousUserInfo.value.anonymousIdentifier : null,
        review: reviewId 
    }
    // If it's a logged user:
    if(userInfo.value) {
        await getUserLikeForReview(reviewId, userInfo.value)
        try {
            // If the review is already liked and the user clicked it, then it has to be deleted
            if (isReviewLikedByUser.value) {
                await deleteLike(currentReviewLike.value.id)
                // Update the like to see the changes in real time
                await getUserLikeForReview(reviewId, userInfo.value)
                isLiked.value = false
                props.review.likes--
    
            // If the review is not yet liked and the user clicked it, then it has to be created
            } else {
                await postLike(likeObj)
                // Update the like to see the changes in real time
                await getUserLikeForReview(reviewId, userInfo.value)
                isLiked.value = true
                props.review.likes++
            }
        } catch(error) {
            console.error(error);
        }
    // If it's an unregistered user:    
    } else {
        await getUserLikeForReview(reviewId, anonymousUserInfo.value)
        try {
            // If the review is already liked and the user clicked it, then it has to be deleted
            if (isReviewLikedByUser.value) {
                await deleteLike(currentReviewLike.value.id)
                // Update the like to see the changes in real time
                await getUserLikeForReview(reviewId, anonymousUserInfo.value)
                isLiked.value = false
                props.review.likes--
            // If the review is not yet liked and the user clicked it, then it has to be created
            } else {
                await postLike(likeObj)
                // Update the like to see the changes in real time
                await getUserLikeForReview(reviewId, anonymousUserInfo.value)
                isLiked.value = true
                props.review.likes++
            } 
        } catch(error) {
            console.error(error);
        }
        
    }

}


const handleConfirmEdit = async () => {
    reviewId.value = props.review.id
    try {
        if (userInfo.value) {
        await updateReview(reviewId.value, props.review, userInfo.value)
    } else if (anonymousUserInfo.value) {
        await updateReview(reviewId.value, props.review, anonymousUserInfo.value)
    }

    } catch(error) {
            console.error(error);
    }

    getPostDetails(props.review.post)

    onEdit.value = false
}


if (userInfo.value) {
    await getUserLikeForReview(props.review.id, userInfo.value)
    isLiked.value = isReviewLikedByUser.value

} else {
    await getUserLikeForReview(props.review.id, anonymousUserInfo.value)
    isLiked.value = isReviewLikedByUser.value
}

const date = new Date(props.review.created_at);
const options = {
  day: "2-digit",
  month: "2-digit",
  year: "numeric",
  hour: "numeric",
  minute: "2-digit",
  hour12: true
};
const formattedDate = date.toLocaleDateString("en-US", options).replace('AM', 'a.m.').replace('PM', 'p.m.');



const handleToggleSureModal = () => {
    reviewId.value = props.review.id
    toggleSureModal()
}

</script>
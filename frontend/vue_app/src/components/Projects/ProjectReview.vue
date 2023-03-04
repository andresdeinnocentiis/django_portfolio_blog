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
                    <p>{{createdAtFormatted}}</p>
                </div>
            </div>
            <div v-else class="user-verified-container">
                <div class="user-verified-img">
                    <font-awesome-icon icon="fa-solid fa-user" />
                </div>
                <div class="user-verified-data">
                    <p class="review-username">{{review.anonymous_user.username}}</p>
                </div>
            </div>
            <StarRating :color="'#27D49F'" :value="review.rating" :className="'single-review'"/>
        </div>
        <p class="review-content">{{review.content}}</p>
        <div class="review-extra-container">
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
                <font-awesome-icon icon="fa-solid fa-trash" class="review-admin-action-btn delete" @click.prevent="toggleSureModal" />
            </div>
        </div>
    </div>
        
    
</template>

<script setup>
import { computed, ref } from "vue";
import { storeToRefs } from "pinia";
import { useReviewsStore } from "../../stores/reviews";
import { useUserLoggedStore } from "../../stores/userLogged";
import { useLikesStore } from "../../stores/likes";
import AreYouSureModal from "../Elements/AreYouSureModal.vue";
import StarRating from '../Elements/StarRating.vue';

const props = defineProps({
    review: {
        type: Object,
        required: true
    }
})

const userLoggedStore = useUserLoggedStore()
const { isUserLogged } = userLoggedStore
const { isUserAdmin, userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)

const reviewsStore = useReviewsStore()
const { getUserReviewsForPost, getReviews } = reviewsStore
const { userReviewsForPost, reviewsList } = storeToRefs(reviewsStore)

const likesStore = useLikesStore()
const { postLike, deleteLike, getUserLikeForReview } = likesStore
const { currentReviewLike, isReviewLikedByUser } = storeToRefs(likesStore)

const isLiked = ref(false)


let createdAtFormatted
createdAtFormatted = computed(() => { 
    if (props.review.created_at) {
        const inputString = props.review.created_at
        const [datePart, timePart] = inputString.split('T');
        const [year, month, day] = datePart.split('-').map(Number);
        const [hours, minutes, seconds] = timePart.slice(0, -1).split(':').map(Number);
        const newDate = new Date(year, month - 1, day, hours, minutes, seconds);
        return newDate.toLocaleDateString('en-GB', { hour:'2-digit', day: '2-digit', month: '2-digit', year: 'numeric' });
    }
})

let isUserOwner 

if (userInfo.value) {
    isUserOwner = props.review.user && props.review.user.id == userInfo.value.id  ? true : false
} else if (anonymousUserInfo.value) {
    isUserOwner = props.review.anonymous_user && props.review.anonymous_user.anonymous_identifier == anonymousUserInfo.value.anonymousIdentifier ? true : false
} else {
    isUserOwner = false
}

const toggleEditReview = () => {}
const toggleSureModal = () => {}


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
    
            // If the review is not yet liked and the user clicked it, then it has to be created
            } else {
                await postLike(likeObj)
                // Update the like to see the changes in real time
                await getUserLikeForReview(reviewId, userInfo.value)
                isLiked.value = true
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
            // If the review is not yet liked and the user clicked it, then it has to be created
            } else {
                await postLike(likeObj)
                // Update the like to see the changes in real time
                await getUserLikeForReview(reviewId, anonymousUserInfo.value)
                isLiked.value = true
            } 
        } catch(error) {
            console.error(error);
        }
        
    }

}


if (userInfo.value) {
    await getUserLikeForReview(props.review.id, userInfo.value)
    isLiked.value = isReviewLikedByUser.value
} else {
    await getUserLikeForReview(props.review.id, anonymousUserInfo.value)
    isLiked.value = isReviewLikedByUser.value
}
</script>
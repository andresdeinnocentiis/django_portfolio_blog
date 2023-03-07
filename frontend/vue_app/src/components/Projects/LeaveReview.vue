<template>
    <div class="leave-review-container">
        <div v-if="!onLeaveReview && !leftReview" class="leave-review-btn" @click.prevent="toggleOnLeaveReview">
            <p class="leave-review-btn-text">Leave a Review!</p>

        </div>
        <div v-else-if="!onLeaveReview && leftReview" class="leave-review-btn review-left">
            <p class="leave-review-btn-text review-left">Looks like you already wrote a review, thanks!!</p>
        </div>
        <div v-else class="leave-review-write">
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
                            <input v-model="newReview.username" type="text" required placeholder="&nbsp;"/>
                            <span class="placeholder">Enter Username</span>
                        </label>
                    </div>
                </div>
                <StarRatingAction color="#27D49F" class="edit-rating rating-newReview" v-model="newReview.rating" @update:value="handleRateReview" />
            </div>
            <label class="custom-field" aria-label="Enter review">
                <textarea style="resize: none;" class="review-edit newReview" autofocus v-model="newReview.content" type="text" required placeholder="&nbsp;" rows="4" cols="50" />
                <span class="placeholder-textarea">Write an amazing review here!</span>
            </label>
            
            <div class="review-extra-container confirm-edit-container">
                <font-awesome-icon icon="fa-solid fa-check" class="review-icon-confirm" @click.prevent="handleConfirmNewReview" />
                <font-awesome-icon icon="fa-solid fa-xmark" class="review-icon-cancel" @click.prevent="cancelEditReview" />
            </div>
            
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, watchEffect } from 'vue';
import { storeToRefs } from 'pinia';
import { useUserLoggedStore } from "../../stores/userLogged";
import { useReviewsStore } from '../../stores/reviews';
import StarRatingAction from '../Elements/StarRatingAction.vue';

const userLoggedStore = useUserLoggedStore()
const { userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)
const { createAnonymousUser } = userLoggedStore

const reviewsStore = useReviewsStore()
const { postReview, getUserReviewsForPost } = reviewsStore
const { currentPostReviews } = storeToRefs(reviewsStore)

const props = defineProps({
    postId: {
        type: String,
        required: true
    }
})

const onLeaveReview = ref(false)

const leftReview = ref(false)

const newReview = ref({
    username: userInfo.value ? userInfo.value.username : anonymousUserInfo.value.username ? anonymousUserInfo.value.username : "",
    content: "",
    rating: 0
})

const toggleOnLeaveReview = () => {
    onLeaveReview.value = !onLeaveReview.value
}

const cancelEditReview = () => {
    onLeaveReview.value = false
    newReview.value.username = userInfo.value && userInfo.value.username ? userInfo.value.username : anonymousUserInfo.value && anonymousUserInfo.value.username ? anonymousUserInfo.value.username : "" 
    newReview.value.content = "" 
    newReview.value.rating = 0
}

const handleRateReview = (value) => {
    newReview.value.rating = value
}

const handleConfirmNewReview = async () => {
    
    if (anonymousUserInfo.value && anonymousUserInfo.value.id) {
        // if it's an anon user and is already on the database:
        const reviewObj = {
            post: props.postId,
            user: null,
            anonymous_user: anonymousUserInfo.value.id,
            content: newReview.value.content,
            rating: newReview.value.rating
        }
        try {
            await postReview(reviewObj, props.postId)
            leftReview.value = true
        } catch(error) {
            console.log(error);
        }

    } else if (userInfo.value) {
        // If it's a registered user:
        const reviewObj = {
            post: props.postId,
            user: userInfo.value.id,
            anonymous_user: null,
            content: newReview.value.content,
            rating: newReview.value.rating
        }

        try {
            await postReview(reviewObj, props.postId)
            leftReview.value = true
        } catch(error) {
            console.log(error);
        }
        
    } else {
        // If it's an anon user and is not yet on the database

        const newAnonUser = {
            username: newReview.value.username,
            anonymous_identifier: anonymousUserInfo.value.anonymous_identifier
        }
        const success = await createAnonymousUser(newAnonUser)
        if (success) {

            const reviewObj = {
                post: props.postId,
                user: null,
                anonymous_user: anonymousUserInfo.value.id,
                content: newReview.value.content,
                rating: newReview.value.rating
            }

            try {
                await postReview(reviewObj, props.postId)
                leftReview.value = true
            } catch(error) {
                console.log(error);
            }

            await userLeftReview()
        }
    }

    onLeaveReview.value = false
    await userLeftReview()
}

const userLeftReview = async () => {
    let response
    if (userInfo.value) {
        response = await getUserReviewsForPost(props.postId, userInfo.value.id, true)
    } else if (anonymousUserInfo.value && anonymousUserInfo.value.id) {
        response = await getUserReviewsForPost(props.postId, anonymousUserInfo.value.id, false)
    } 

    leftReview.value = response
}

await userLeftReview()

onMounted(async () => {

  await userLeftReview()

})

watchEffect(async () => {
    currentPostReviews.value
    await userLeftReview()
})
</script>
<template>
    <div class="reviews-section-container">
        <h1 class="posts__title">Reviews</h1>
        <div class="reviews-container">
            <div v-for="(review, index) in currentPostReviews" :key="index" class="review">
                <div class="review-header">
                    
                    <div v-if="review.user" class="user-verified-container">
                        <div class="user-verified-img">
                            <img v-if="review.user.image" :src="review.user.image" alt="">
                            <font-awesome-icon icon="fa-solid fa-user" v-else />
                        </div>
                        <div class="user-verified-data">
                            <p class="review-username">{{review.user.username}}</p>
                            <font-awesome-icon icon="fa-solid fa-circle-check" />
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
            </div>
        </div>
    </div>
</template>


<script setup>
import { defineProps, computed, ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useReviewsStore } from '../../stores/reviews';
import { useLikesStore } from '../../stores/likes';
import { useUserLoggedStore } from "../../stores/userLogged";
import StarRatingAction from '../Elements/StarRatingAction.vue';
import StarRating from '../Elements/StarRating.vue';

const props = defineProps({
    id: {
        type: String,
        required: true
    }
})

const reviewsStore = useReviewsStore()
const { getReviewsForPost, getUserReviewsForPost, postReview, updateReview, deleteReview } = reviewsStore
const { reviewsList, currentPostReviews } = storeToRefs(reviewsStore)


await getReviewsForPost(Number(props.id))



</script>
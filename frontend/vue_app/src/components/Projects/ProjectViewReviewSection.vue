<template>
    <div class="reviews-section-container">
        <div class="reviews-container">
            <div v-for="(review, index) in currentPostReviews" :key="index" class="review">
                <div class="review-header">
                    <StarRating :color="'#27D49F'" :value="review.rating" :className="'single-review'"/>
                    <div v-if="review.user" class="user-verified-container">
                        <p>{{review.user.username}}</p>
                        <font-awesome-icon icon="fa-solid fa-circle-check" />
                    </div>
                    <p v-else>{{review.anonymous_user.username}}</p>
                </div>
                <p>{{review.content}}</p>
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
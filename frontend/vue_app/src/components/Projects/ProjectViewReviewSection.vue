<template>
    <div class="reviews-section-container">
        <h1 class="posts__title">Reviews ({{countReviews}})</h1>
        <div class="reviews-container">
            <ProjectReview v-for="(review, index) in currentPostReviews" :key="review.id" class="review" :review="review" />
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
import ProjectReview from './ProjectReview.vue';

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
const countReviews = currentPostReviews.value.length



</script>
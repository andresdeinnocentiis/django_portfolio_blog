<template>
    <div class="reviews-section-container">
        <h1 class="posts__title">Reviews ({{countReviews}})</h1>
        <div class="reviews-container">
            <ProjectReview 
                v-for="review in currentPostReviews" :key="review.id" 
                class="review" 
                :review="review" 
                ref="childComponentRef"    
            />
        </div>
    </div>
    <AreYouSureModal 
        :action="'delete'"
        :method="handleDeleteReview"
    />
</template>


<script setup>
import { defineProps, ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useReviewsStore } from '../../stores/reviews';
import { useUserLoggedStore } from '../../stores/userLogged';
import ProjectReview from './ProjectReview.vue';
import AreYouSureModal from '../Elements/AreYouSureModal.vue';



const props = defineProps({
    id: {
        type: String,
        required: true
    }
})

const reviewsStore = useReviewsStore()
const { getReviewsForPost, deleteReview } = reviewsStore
const { currentPostReviews, reviewId } = storeToRefs(reviewsStore)

const userLoggedStore = useUserLoggedStore()
const { userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)


await getReviewsForPost(Number(props.id))
const countReviews = currentPostReviews.value.length

const tsxModalMsg = ref({
    title: "",
    msg: "",
    variant: "",
    success: false
})


const handleDeleteReview = async () => {
    if (userInfo.value) {
        await deleteReview(reviewId.value, Number(props.id), userInfo.value)
    } else if (anonymousUserInfo.value) {
        await deleteReview(reviewId.value, Number(props.id), anonymousUserInfo.value)
    }
    reviewId.value = null
}

</script>
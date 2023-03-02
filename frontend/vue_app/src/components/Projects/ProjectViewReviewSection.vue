<template>
    <div>
        
    </div>
</template>


<script setup>
import { defineProps, computed, ref } from 'vue';
import { useReviewsStore } from '../../stores/reviews';
import { useLikesStore } from '../../stores/likes';
import { useUserLoggedStore } from "../../stores/userLogged";

const props = defineProps({
    id: {
        type: String,
        required: true
    }
})
</script>
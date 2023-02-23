<template>
    <div class="hashtags-container">
        <div v-for="(hashtag, index) in hashtagsArray" :key="index" class="hashtag-box">
            <p class="hashtag-text">#{{hashtag.toLowerCase()}}</p>
        </div>
   </div>
</template>


<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    hashtagsArray: Array
})
</script>
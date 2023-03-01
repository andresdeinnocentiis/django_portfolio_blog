<template>
    <transition v-if="animate">
        <div class="blob-container">
            <div 
                class="blob"
                :class="`${blobClassName}-blob`"
                :style="{
                    'background': `${background}`, 
                    'border-radius': `${topLeft[0]}% ${topRight[0]}% ${bottomRight[0]}% ${bottomLeft[0]}% / ${topLeft[1]}% ${topRight[1]}% ${bottomRight[1]}% ${bottomLeft[1]}%`,
                    'width': `${width}rem`,
                    'height': `${height}rem`,
                }"
                    
            >
            </div>
            <div v-if="image" class="blob-image-container" :class="`container-${imageClassName}`">
                <img :src="getImageURL(image)" alt="imageAlt"  class="blob-image-img" :class="`img-${imageClassName}`">
            </div>
        </div>
    </transition>
    
    <div v-else class="blob-container" :class="`blob-container-${blobClassName}`">
        <div 
            
            class="blob"
            :class="`${blobClassName}-blob`"
            :style="{
                'background': background, 
                'border-radius': `${topLeft[0]}% ${topRight[0]}% ${bottomRight[0]}% ${bottomLeft[0]}% / ${topLeft[1]}% ${topRight[1]}% ${bottomRight[1]}% ${bottomLeft[1]}%`,
                'width': `${width}rem`,
                'height': `${height}rem`,
            }"
            
        >  
        </div>
        <div v-if="image" class="blob-image-container" :class="`container-${imageClassName}`">
            <img :src="getImageURL(image)" alt="imageAlt" class="blob-image-img" :class="`img-${imageClassName}`">
        </div>
    </div>
</template>



<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    animate: Boolean,
    topLeft: Array,
    topRight: Array,
    bottomRight: Array,
    bottomLeft: Array,
    width: Number,
    height: Number,
    background: String,
    blobClassName: String,
    image: String,
    imageAlt: String,
    imageClassName: String,
})

const getImageURL = (imageName) => {
    return new URL(`../../assets/images/${imageName}`, import.meta.url)
}


</script>
<template>
    <main class="main-home">
        <Hero />
        <Blob
            v-if="!isMobile"
            :animate="true"
            :background="'#00FF9D'"
            :top-left="[67, 57]"
            :top-right="[33, 62]"
            :bottom-right="[26, 38]"
            :bottom-left="[74, 43]"
            :blobClassName="'home-main'"
            :image="'4K_andresdeinnocentiis_BLOB2.png'"
            :imageAlt="'Andres De Innocentiis Main Image'"
            :imageClassName="'main-blob-image'"
        />
    </main>
</template>


<script setup>
import { ref } from 'vue'
import Blob from '../Elements/Blob.vue';
import Hero from '../Elements/Hero.vue';

const isMobile = ref(window.innerWidth <= 900);
window.addEventListener('resize', () => {
  isMobile.value = window.innerWidth <= 900;
});
</script>
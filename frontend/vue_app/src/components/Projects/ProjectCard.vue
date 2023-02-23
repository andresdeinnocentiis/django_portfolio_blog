<template>
    <router-link :to="{name: 'project', params: {id: project.id}}"  class="project-card" 
        :class="{'project-card-dark': !isDarkMode, 'project-card-light': isDarkMode}"
    >
        <div class="project-img-container">
            <img :src="project.image" :alt="project.title" class="project-img">
        </div>
        <div class="project-rest-container">
            <h3 class="project-title" :class="{'light-theme-text': isDarkMode, 'dark-theme-text': !isDarkMode}">{{project.title}}</h3>
            <h5 class="project-caption" :class="{'light-theme-text': isDarkMode, 'dark-theme-text': !isDarkMode}">{{project.caption}}</h5>
            <div class="project-last-part">
                <div class="project-tech-used" :class="{'light-theme-text': isDarkMode, 'dark-theme-text': !isDarkMode}">{{project.tech_used}}</div>
                <div class="project-rating">{{project.rating}}</div>
            </div>
        </div>
    </router-link>
</template>

<script setup>
import { useDarkModeStore } from '../../stores/darkMode';
import { storeToRefs } from 'pinia';
import { defineProps } from 'vue';

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

const props = defineProps({
    project: Object
})

</script>
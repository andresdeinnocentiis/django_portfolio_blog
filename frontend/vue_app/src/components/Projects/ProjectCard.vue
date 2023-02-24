<template>
    <router-link :to="{name: 'project', params: {id: project.id}}" class="project-card" 
        :class="{'project-card-dark': !isDarkMode, 'project-card-light': isDarkMode}"
    >
        <div class="project-img-container">
            <img :src="project.image" :alt="project.title" class="project-img">
        </div>
        <div class="project-rest-container">
            <h3 class="project-title" :class="{'light-theme-text': isDarkMode, 'dark-theme-text': !isDarkMode}">{{project.title}}</h3>
            <h5 class="project-caption" :class="{'light-theme-text': isDarkMode, 'dark-theme-text': !isDarkMode}">{{project.caption}}</h5>
            <div class="project-last-part">
                <div class="project-tech-used" :class="{'light-theme-text': isDarkMode, 'dark-theme-text': !isDarkMode}"><Hashtag :hashtagsArray="arr_tech_used" /></div>
                
                
                <div class="project-rating"><StarRating :value="project.rating" color='#00FF9D' /></div>
                    
                

            </div>
        </div>
    </router-link>
</template>

<script setup>
import { useDarkModeStore } from '../../stores/darkMode';
import { useUserLoggedStore } from '../../stores/userLogged';
import { storeToRefs } from 'pinia';
import { defineProps, computed } from 'vue';
import StarRating from '../Elements/StarRating.vue';
import Hashtag from '../Elements/Hashtag.vue';

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

const userLoggedStore = useUserLoggedStore()
const {isUserAdmin} = storeToRefs(userLoggedStore)

const props = defineProps({
    project: Object
})

const arr_tech_used = computed(() => props.project.tech_used.split(",").map((str) => str.trimStart())) 




</script>
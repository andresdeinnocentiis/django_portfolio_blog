<template>

    <div class="project-container">
        <div class="container__main-division">

            <div class="main-division__first">

                <div class="main-division__first__top">
                    <p class="project-index-container" :class="{'project-index-container-dark': isDarkMode, 'project-index-container-light': !isDarkMode}">
                        {{formattedNumber}}
                    </p>

                    <div class="first__img-container">
                        <img :src="currentPost.image" :alt="currentPost.title" class="current-project-img" :class="{'current-project-img-dark': isDarkMode, 'current-project-img-light': !isDarkMode}">
                    </div>
                    <div class="img-overlay-description" :class="{'img-overlay-description-dark': isDarkMode, 'img-overlay-description-light': !isDarkMode}">
                        <h3 class="current-post-title">{{currentPost.title}}</h3>
                        <p class="current-post-description">{{currentPost.description}}</p>
                    </div>
                    

                </div>
                <div class="main-division__first__bottom">
                    <div class="post-user-actions-container"  :class="{'img-overlay-description-dark': isDarkMode, 'img-overlay-description-light': !isDarkMode}">
                        <p :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}"><StarRatingAction /></p>
                        <font-awesome-icon class="like-action" v-if="isPostLikedByUser" icon="fa-solid fa-heart" :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}" />
                        <font-awesome-icon class="like-action" v-else icon="fa-regular fa-heart" :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}" />
                        
                    </div>
                </div>

            </div>
            <div class="main-division__second">
                <div class="second__container" >

                    <div class="project-data" :class="{'img-overlay-description-dark': isDarkMode, 'img-overlay-description-light': !isDarkMode}">
                        <div class="project-data__top">
                            <h3>{{currentPost.title}}</h3>
                            <h4>Tech used:</h4>
                            <p class="single-project-link developed-for" v-if="currentPost.developed_for">Developed for: <a :href="currentPost.developed_for_link">{{currentPost.developed_for}}</a></p>
                            <Hashtag :hashtagsArray="arr_tech_used" class="hashtag-text-project" />
                            <p class="single-project-link github-link" v-if="currentPost.github_link">Github: <a :href="currentPost.github_link">{{currentPost.github_link}}</a></p>
                            <p class="single-project-link website-link" v-if="currentPost.website_link">Website: {{currentPost.website_link}}</p>
                            
                            <p class="created-at">
                                {{ currentPost.createdAt }}
                            </p>
    
                        </div>
                        <div class="project-data__bottom" :class="{'project-data__bottom-dark': isDarkMode, 'project-data__bottom-light': !isDarkMode}">
                            <p class="total-data"><span :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}">{{currentPost.rating}}</span> / 5 <span :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}"><font-awesome-icon icon="fa-solid fa-star"/></span></p>
                            <p class="total-data"><span :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}">{{currentPost.num_reviews}}</span> {{currentPost.num_reviews.length == 1 ? 'review' : 'reviews'}}</p>
                            <p class="total-data"><span :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}">{{currentPost.likes}}</span> {{currentPost.likes.length == 1 ? 'like' : 'likes'}}</p>
                        </div>
                    </div>
                    <div v-if="userInfo && isUserAdmin" class="post-admin-actions-container" :class="{'img-overlay-description-dark': isDarkMode, 'img-overlay-description-light': !isDarkMode}">
                        <font-awesome-icon icon="fa-solid fa-pen-to-square" class="post-admin-action-btn edit" />
                        <font-awesome-icon icon="fa-solid fa-trash" class="post-admin-action-btn delete" />
                    </div>

                </div>
            </div>
        </div>
    </div>
    
</template>

<script setup>
import { defineProps, computed } from 'vue';
import { storeToRefs } from 'pinia';
import { usePostsStore } from "../stores/posts"
import { useUserLoggedStore } from "../stores/userLogged";
import { useDarkModeStore } from '../stores/darkMode';
import Hashtag from '../components/Elements/Hashtag.vue';
import StarRatingAction from '../components/Elements/StarRatingAction.vue';

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

const postsStore = usePostsStore()
const { getPostDetails, getIsPostLikedByUser } = postsStore
const { currentPost, isPostLikedByUser } = storeToRefs(postsStore)
const userLoggedStore = useUserLoggedStore()
const { isUserAdmin, userInfo } = storeToRefs(userLoggedStore)

const props = defineProps({
    id: {
        type: String,
        required: true
    }
})

const formattedNumber = props.id.toString().padStart(2, "0")

const arr_tech_used = computed(() => currentPost.value.tech_used.split(",").map((str) => str.trimStart())) 


getPostDetails(Number(props.id))

getIsPostLikedByUser(Number(props.id), userInfo.value.id)




</script>
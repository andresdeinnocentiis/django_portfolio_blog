<template>

    <div class="project-container">
        <div class="container__main-division">

            <div class="main-division__first">

                <div class="main-division__first__top">

                    <div class="first__img-container">
                        <img :src="currentPost.image" :alt="currentPost.title" class="current-project-img">
                    </div>
                    <div class="img-overlay-description">
                        <h3>{{currentPost.title}}</h3>
                        <p>{{currentPost.description}}</p>
                    </div>
                    <div class="project-index-container">
                        <p class="post-index">{{formattedNumber}}</p>
                    </div>

                </div>
                <div class="main-division__first__bottom">
                    <div class="post-user-actions-container">
                        <p>{{currentPost.rating}}</p>
                        <font-awesome-icon v-if="isPostLikedByUser" icon="fa-solid fa-heart" />
                        <font-awesome-icon v-else icon="fa-regular fa-heart" />
                        
                    </div>
                </div>

            </div>
            <div class="main-division__second">
                <div class="project-data">
                    <div class="project-data__top">
                        
                        <p class="developed-for" v-if="currentPost.developed_for">{{developed_for}}</p>
                        <Hashtag :hashtagsArray="arr_tech_used" />


                        <p class="github-link" v-if="currentPost.github_link">{{github_link}}</p>
                        <p class="website-link" v-if="currentPost.website_link">{{website_link}}</p>
                        
                        <p class="created-at">
                            {{ currentPost.createdAt }}
                        </p>

                    </div>
                    <div class="project-data__bottom">
                        <p class="total-reviews">{{currentPost.num_reviews}}{{currentPost.num_reviews.length == 1 ? 'review' : 'reviews'}}</p>
                        <p class="total-likes">{{currentPost.likes}}{{currentPost.likes.length == 1 ? 'like' : 'likes'}}</p>
                    </div>
                </div>
                <div class="post-admin-actions-container">
                    <font-awesome-icon icon="fa-solid fa-pen-to-square" />
                    <font-awesome-icon icon="fa-solid fa-trash" />
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
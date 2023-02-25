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
                    <div class="post-actions-container">

                    </div>
                </div>

            </div>
            <div class="main-division__second">
                <div class="project-data">

                </div>
            </div>
        </div>
    </div>
    
</template>

<script setup>
import { defineProps } from 'vue';
import { storeToRefs } from 'pinia';
import { usePostsStore } from "../stores/posts"
import { useUserLoggedStore } from "../stores/userLogged";
import { useDarkModeStore } from '../stores/darkMode';
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

getPostDetails(Number(props.id))

getIsPostLikedByUser(Number(props.id), userInfo.value.id)

console.log("IS LIKED BY USER: ", isPostLikedByUser.value);

</script>
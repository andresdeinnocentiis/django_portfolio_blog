<template>
    <div class="container__main-division">

        <div class="main-division__first">

            <div class="main-division__first__top">

                <div class="first__img-container">
                    <img :src="currentPost.image" :alt="currentPost.title" class="current-project-img" :class="{'current-project-img-dark': isDarkMode, 'current-project-img-light': !isDarkMode}">
                </div>
                <Tilt 
                    :options="{scale:1,startX:0,transition: true, glare: true, }" :parallax="true"
                    class="img-overlay-description" 
                    :class="{'img-overlay-description-dark': isDarkMode, 'img-overlay-description-light': !isDarkMode}"
                >
                    <div 
                    class="tilt-card"
                    >
                        <h3 class="current-post-title">{{currentPost.title}}</h3>
                        <p class="current-post-description">{{currentPost.description}}</p>
                    </div>
                </Tilt>

            </div>
            <div class="main-division__first__bottom">
                <div class="post-user-actions-container"  :class="{'img-overlay-description-dark': isDarkMode, 'img-overlay-description-light': !isDarkMode}">
                    <p :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}">
                        <StarRating :color="'#27D49F'" :value="userRating" v-bind="userRating" :className="'user-rating'"/>
                    </p>
                    <div class="like-icon-div" @click.prevent="handleLikeClick">
                        <font-awesome-icon class="like-action" v-if="isPostLikedByUser" icon="fa-solid fa-heart" :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}" />
                        <font-awesome-icon class="like-action" v-else icon="fa-regular fa-heart" :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}" />
                    </div>
                </div>
            </div>

        </div>
        <div class="main-division__second">
            
            <div class="second__container" >

                <Tilt class="project-data" :class="{'img-overlay-description-dark': isDarkMode, 'img-overlay-description-light': !isDarkMode}"
                    :options="{scale:1,startX:0,transition: true, glare: true, }" :parallax="true"
                >
                    <div class="project-data__top">
                        <h3>{{currentPost.title}}</h3>
                        <h4>Tech used:</h4>
                        <Hashtag :hashtagsArray="arr_tech_used" class="hashtag-text-project" />
                        <p class="single-project-link developed-for" v-if="currentPost.developed_for"><span>Developed for: </span><a class="text-project-link" :href="currentPost.developed_for_link">{{currentPost.developed_for}}</a></p>
                        <p class="single-project-link github-link" v-if="currentPost.github_link"><span>Github: </span><a class="text-project-link" :href="currentPost.github_link">{{currentPost.github_link}}</a></p>
                        <p class="single-project-link website-link" v-if="currentPost.website_link"><span>Website: </span><a class="text-project-link" :href="currentPost.website_link">{{currentPost.website_link}}</a></p>
                        
                        <p class="created-at">
                            <span>Created at: </span>{{ createdAtFormatted }}
                        </p>
                        <p class="project-status">
                            <span>Status: </span><span style="font-weight: 700" :style="{color: currentPost.status === 'Completed' ? '#27D49F' : 'In Progress' ? '#D79743' : '#DC1957'}">{{ currentPost.status }}</span>
                        </p>

                    </div>
                    <div class="project-data__bottom" :class="{'project-data__bottom-dark': isDarkMode, 'project-data__bottom-light': !isDarkMode}">
                        <p class="total-data"><span 
                            :style="{color: currentPost.rating >= 4 ? '#27D49F' : currentPost.rating >= 2 ? '#d79743' : '#DC1957'}"
                        >{{currentPost.rating}}</span> / 5 <span :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}"><font-awesome-icon icon="fa-solid fa-star"/></span></p>
                        <p class="total-data"><span :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}">{{currentPost.num_reviews}}</span> {{currentPost.num_reviews.length == 1 ? 'review' : 'reviews'}}</p>
                        <p class="total-data"><span :class="{'dark-span': isDarkMode, 'light-span': !isDarkMode}">{{currentPost.likes}}</span> {{currentPost.likes.length == 1 ? 'like' : 'likes'}}</p>
                    </div>
                </Tilt>
                <div v-if="userInfo && isUserAdmin" class="post-admin-actions-container" :class="{'img-overlay-description-dark': isDarkMode, 'img-overlay-description-light': !isDarkMode}">
                    <font-awesome-icon icon="fa-solid fa-pen-to-square" class="post-admin-action-btn edit" @click.prevent="toggleEditProjectModal"/>
                    <font-awesome-icon icon="fa-solid fa-trash" class="post-admin-action-btn delete" @click.prevent="toggleSureModal" />
                </div>

            </div>
            
        </div>
    </div>
    
    <!-- Are You Sure Modal [for yes or no on some action (delete or edit)] -->
    <AreYouSureModal 
        :action="'delete'" 
        :method="handleDeleteProject" 
    />
 
    <!-- Transaction Result Modal [for delete or edit success or error] -->
    <TransactionModal 
        :success="tsxModalMsg.success"
        :variant="tsxModalMsg.variant" 
        :title="tsxModalMsg.title" 
        :message="tsxModalMsg.msg" 
    />
    
    <!-- Edit Project [Modal] -->
    <ProjectEditModal />

</template>

<script setup>
import { defineProps, computed, ref, watchEffect } from 'vue';
import { storeToRefs } from 'pinia';
import { usePostsStore } from '../../stores/posts';
import { useReviewsStore } from '../../stores/reviews';
import { useLikesStore } from '../../stores/likes';
import { useUserLoggedStore } from "../../stores/userLogged";
import { useDarkModeStore } from '../../stores/darkMode';
import { useModalStore } from '../../stores/modal';
import Hashtag from '../Elements/Hashtag.vue';
import StarRating from '../Elements/StarRating.vue';
import AreYouSureModal from '../Elements/AreYouSureModal.vue';
import ProjectEditModal from './ProjectEditModal.vue'
import TransactionModal from '@/components/Elements/TransactionModal.vue';
import Tilt from 'vanilla-tilt-vue'



const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

const postsStore = usePostsStore()
const { getPostDetails, getIsPostLikedByUser, deletePost } = postsStore
const { currentPost, isPostLikedByUser } = storeToRefs(postsStore)

const reviewsStore = useReviewsStore()
const { getUserReviewsForPost, getReviews } = reviewsStore
const { userReviewsForPost, reviewsList } = storeToRefs(reviewsStore)

const likesStore = useLikesStore()
const { getLikes, postLike, deleteLike, getUserLikeForPost } = likesStore
const { likesList, currentPostLikeId } = storeToRefs(likesStore)

const userLoggedStore = useUserLoggedStore()
const { isUserLogged } = userLoggedStore
const { isUserAdmin, userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)

const modalStore = useModalStore()
const { toggleEditProjectModal, toggleTsxModal, toggleSureModal } = modalStore


const tsxModalMsg = ref({
    title: "",
    msg: "",
    variant: "",
    success: false
})


const rating = ref(0)

let userRating = 0

const props = defineProps({
    id: {
        type: String,
        required: true
    }
})


// HANDLE FUNCTIONS:
// Function to get the value from the child component StarRatingAction
const handleUpdateValue = (value) => {
    rating.value = value
}

const handleLikeClick = async () => {

    // Create the Like Object that would be sent if the request is POST
    const likeObj = {
        user: userInfo.value ? userInfo.value.id : null,
        anonymous_identifier: anonymousUserInfo.value ? anonymousUserInfo.value.anonymous_identifier : null,
        post: currentPost.value.id 
    }
    // If it's a logged user:
    if(userInfo.value) {
        try {
            // If the post is already liked and the user clicked it, then it has to be deleted
            if (isPostLikedByUser.value) {
                await deleteLike(currentPostLikeId.value)
                // Update everything in the page to see the changes in real time
                isPostLikedByUser.value = false
                await getPostDetails(Number(props.id))
                await getLikes()
                await getUserLikeForPost(Number(props.id), userInfo)
            // If the post is not yet liked and the user clicked it, then it has to be created
            } else {
                await postLike(likeObj)
                // Update everything in the page to see the changes in real time
                isPostLikedByUser.value = !isPostLikedByUser.value
                await getPostDetails(Number(props.id))
                await getLikes()
                await getUserLikeForPost(Number(props.id), userInfo)
    
            }
        } catch(error) {
            console.error(error);
        }
    // If it's an unregistered user:    
    } else {
        try {
            // If the post is already liked and the user clicked it, then it has to be deleted
            if (isPostLikedByUser.value) {
                await deleteLike(currentPostLikeId.value)
                // Update everything in the page to see the changes in real time
                isPostLikedByUser.value = false
                await getPostDetails(Number(props.id))
                await getLikes()
                await getUserLikeForPost(Number(props.id), anonymousUserInfo)

            // If the post is not yet liked and the user clicked it, then it has to be created
            } else {
                await postLike(likeObj)
                // Update everything in the page to see the changes in real time
                isPostLikedByUser.value = !isPostLikedByUser.value
                await getPostDetails(Number(props.id))
                await getLikes()
                await getUserLikeForPost(Number(props.id), anonymousUserInfo)
    
            } 
        } catch(error) {
            console.error(error);
        }
        
    }

}

const handleDeleteProject = async () => {
    const success = await deletePost(props.id)

    if (success) {

        tsxModalMsg.value.success = true
        tsxModalMsg.value.variant = "success"
        tsxModalMsg.value.title = "Success!"
        tsxModalMsg.value.msg = "The project was deleted successfully!"
        toggleTsxModal()
        setTimeout(() => {
            tsxModalMsg.value.success = false
            tsxModalMsg.value.variant = ""
            tsxModalMsg.value.title = ""
            tsxModalMsg.value.msg = ""
            toggleTsxModal()
            }, 3000)
    } else {
        
        tsxModalMsg.value.success = false
        tsxModalMsg.value.variant = "danger"
        tsxModalMsg.value.title = "Error."
        tsxModalMsg.value.msg = "Something wen't wrong when trying to delete the project. Please try again."
        toggleTsxModal()
        setTimeout(() => {
            tsxModalMsg.value.success = false
            tsxModalMsg.value.variant = ""
            tsxModalMsg.value.title = ""
            tsxModalMsg.value.msg = ""
                toggleTsxModal()
            }, 3000)
    }
}

// Create an array of all the tech I used for the project so I can style each of them individually
let arr_tech_used
arr_tech_used = computed(() => {

  if (currentPost.value.tech_used) {
    return currentPost.value.tech_used.split(",").map((str) => str.trimStart())
  } else {
    return []
  }

})

// Here I formatted the datetime to "DD/MM/YYYY" because of the format that comes from the API
let createdAtFormatted
createdAtFormatted = computed(() => { 
    if (currentPost.value.created_at) {
        const inputString = currentPost.value.created_at
        const [datePart, timePart] = inputString.split('T');
        const [year, month, day] = datePart.split('-').map(Number);
        const [hours, minutes, seconds] = timePart.slice(0, -1).split(':').map(Number);
        const newDate = new Date(year, month - 1, day, hours, minutes, seconds);
        return newDate.toLocaleDateString('en-GB', { day: '2-digit', month: '2-digit', year: 'numeric' });
    }
})


await getPostDetails(Number(props.id))

const isPostLiked = async () => {
    if (userInfo.value) {
        await getIsPostLikedByUser(Number(props.id), userInfo)
    } else if (anonymousUserInfo.value) {
        await getIsPostLikedByUser(Number(props.id), anonymousUserInfo)
    } else {
        isPostLikedByUser.value = false
    }
}

const getUserOrAnonUserId = () => {
    let id
    if(isUserLogged()) {
        id = userInfo.value.id
    } else {
        id = anonymousUserInfo.value.id
    }

    return id
}

 

await isPostLiked()
if (userInfo.value || anonymousUserInfo.value.id) {
    await getUserReviewsForPost(currentPost.value.id, getUserOrAnonUserId(), isUserLogged())
}
await getLikes()


if (userReviewsForPost.value) {
    userRating = userReviewsForPost.value.rating // I had to do this in order to pass it as prop to the <StarRating /> component
}


if (userInfo.value) {
    await getUserLikeForPost(Number(props.id), userInfo)
} else if (anonymousUserInfo.value) {
    await getUserLikeForPost(Number(props.id), anonymousUserInfo)
}

watchEffect(() => {
    userReviewsForPost.value
    rating.value
    userRating
})

</script>

<style>
.project-index-container-dark::before {
    content: attr(data-content);
    position: absolute;
    top: .3rem;
    right: .3rem;
    color: var(--textSecondary);
}

.project-index-container-light::before {
    content: attr(data-content);
    position: absolute;
    top: .5rem;
    right: .5rem;
    color: wheat;
}
.project-index-container-dark[data-content=""]::before {
    content: attr(data-content, counter(projectIndex));
}
.project-index-container-light[data-content=""]::before {
    content: attr(data-content, counter(projectIndex));
}

</style>
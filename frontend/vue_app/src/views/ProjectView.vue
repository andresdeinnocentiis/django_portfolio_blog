<template>

    <div class="project-container">
        <Suspense>
            <ProjectViewMain :id="props.id" />
            <template #fallback>
                <p>Loading...</p>
            </template>
        </Suspense>
    </div>
    
</template>

<script setup>
import { defineProps, computed, defineAsyncComponent } from 'vue';
import { storeToRefs } from 'pinia';
import { usePostsStore } from "../stores/posts"
import { useUserLoggedStore } from "../stores/userLogged";
import { useDarkModeStore } from '../stores/darkMode';



const ProjectViewMain = defineAsyncComponent(() => 
    import('../components/Projects/ProjectViewMain.vue')
)

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

const postsStore = usePostsStore()

const userLoggedStore = useUserLoggedStore()
const { isUserAdmin, userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)


const props = defineProps({
    id: {
        type: String,
        required: true
    }
})



</script>
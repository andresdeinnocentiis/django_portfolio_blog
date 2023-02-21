<template>
    <li class="nav-item">
        <router-link 
            :to="{name: item.routeName}"
            class="nav-link"    
            :class="{'dark-theme-link':darkModeStore.isDarkMode, 'light-theme-link':!darkModeStore.isDarkMode}"
        >
        {{item.name}}
        </router-link> 
    </li>
</template>

<script setup>
import { useDarkModeStore } from '../../stores/darkMode';

const darkModeStore = useDarkModeStore()

const props = defineProps({
    item: {
        type: Object,
        required: true,
    }
})

</script>
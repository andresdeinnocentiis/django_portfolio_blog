<template>
    <div 
        class="add-btn"
        :class="`add-${btnName}-btn add-${btnName}-btn-${color}`"
        :style="`background-color:${color}`"
        >
        <font-awesome-icon icon="fa-solid fa-plus" class="plus-icon" :class="`plus-icon-${btnName}`" />
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    btnName: String,
    color: String
})
</script>
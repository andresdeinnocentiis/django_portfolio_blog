<template>
    <div :class="`rating ${className}`">
        <span :style="{'color':color}">
            <font-awesome-icon v-if="value >=1" icon="fa-solid fa-star" />
            <font-awesome-icon v-else-if="value>=0.5" icon="fa-regular fa-star-half-stroke" />
            <font-awesome-icon v-else icon="fa-regular fa-star" />   
        </span>
        <span :style="{'color':color}">
            <font-awesome-icon v-if="value >=2" icon="fa-solid fa-star" />
            <font-awesome-icon v-else-if="value>=1.5" icon="fa-regular fa-star-half-stroke" />
            <font-awesome-icon v-else icon="fa-regular fa-star" />   
        </span>
        <span :style="{'color':color}">
            <font-awesome-icon v-if="value >=3" icon="fa-solid fa-star" />
            <font-awesome-icon v-else-if="value>=2.5" icon="fa-regular fa-star-half-stroke" />
            <font-awesome-icon v-else icon="fa-regular fa-star" />   
        </span>
        <span :style="{'color':color}">
            <font-awesome-icon v-if="value >=4" icon="fa-solid fa-star" />
            <font-awesome-icon v-else-if="value>=3.5" icon="fa-regular fa-star-half-stroke" />
            <font-awesome-icon v-else icon="fa-regular fa-star" />   
        </span>
        <span :style="{'color':color}">
            <font-awesome-icon v-if="value >=5" icon="fa-solid fa-star" />
            <font-awesome-icon v-else-if="value>=4.5" icon="fa-regular fa-star-half-stroke" />
            <font-awesome-icon v-else icon="fa-regular fa-star" />   
        </span>
        
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    value: Number,
    color: String,
    className: String
})


</script>
<template>
    <div class="star-rating-container">
        <div class="rating-wrap">
            <span class="star-hover star-hover1" ref="halfStar1" @click="handleClick($event)">
                <font-awesome-icon v-if="value >=1" icon="fa-solid fa-star fullStar star-icon" />
                <font-awesome-icon v-else-if="value>=0.5" icon="fa-regular fa-star-half-stroke halfStar star-icon" />
                <font-awesome-icon v-else icon="fa-regular fa-star emptyStar star-icon" />   
            </span>
            <span class="star-hover star-hover2">
                <font-awesome-icon v-if="value >=2" icon="fa-solid fa-star fullStar star-icon" />
                <font-awesome-icon v-else-if="value>=1.5" icon="fa-regular fa-star-half-stroke halfStar star-icon" />
                <font-awesome-icon v-else icon="fa-regular fa-star emptyStar star-icon" />   
            </span>
            <span class="star-hover star-hover3">
                <font-awesome-icon v-if="value >=3" icon="fa-solid fa-star fullStar star-icon" />
                <font-awesome-icon v-else-if="value>=2.5" icon="fa-regular fa-star-half-stroke halfStar star-icon" />
                <font-awesome-icon v-else icon="fa-regular fa-star emptyStar star-icon" />   
            </span>
            <span class="star-hover star-hover4">
                <font-awesome-icon v-if="value >=4" icon="fa-solid fa-star fullStar star-icon" />
                <font-awesome-icon v-else-if="value>=3.5" icon="fa-regular fa-star-half-stroke halfStar star-icon" />
                <font-awesome-icon v-else icon="fa-regular fa-star emptyStar star-icon" />   
            </span>
            <span class="star-hover star-hover5">
                <font-awesome-icon v-if="value >=5" icon="fa-solid fa-star fullStar star-icon" />
                <font-awesome-icon v-else-if="value>=4.5" icon="fa-regular fa-star-half-stroke halfStar star-icon" />
                <font-awesome-icon v-else icon="fa-regular fa-star emptyStar star-icon" />   
            </span>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, defineProps } from 'vue';

const props = defineProps({
    color: String
})

const value = ref(0)
const halfStar1 = ref('halfStar1');



const handleClick = (e) => {
    console.log("TARGET: ", e.target);
    if(e.target.classList.contains('star-hover1') && e.target.before) {
            value.value = 0.5
    } else if(e.target.classList.contains('star-hover1') && !e.target.before) {
            value.value = 1
    }

    console.log(value.value);
}


</script>

<style>
.star-hover:hover, .star-hover:focus {
    cursor: pointer;
}

.star-hover1,.star-hover2,.star-hover3,.star-hover4,.star-hover5 {
    position: relative;
}

.star-hover1::before {
    content:" ";
    width: 50%;
    height: 100%;
    position: absolute;
    background-color: red;
    left: 0;
}

.star-hover2::before {
    content:" ";
    width: 50%;
    height: 100%;
    position: absolute;
    background-color: red;
    left: 0;
}

.star-hover3::before {
    content:" ";
    width: 50%;
    height: 100%;
    position: absolute;
    background-color: red;
    left: 0;
}

.star-hover4::before {
    content:" ";
    width: 50%;
    height: 100%;
    position: absolute;
    background-color: red;
    left: 0;
}

.star-hover5::before {
    content:" ";
    width: 50%;
    height: 100%;
    position: absolute;
    background-color: red;
    left: 0;
}



</style>
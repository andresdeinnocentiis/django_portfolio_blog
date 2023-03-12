<template>
    <div class="exp-section-container">
        <div class="exp-img-container">
            <img :src="getImageURL('Foto1.jpg')" alt="Andres De Innocentiis image" class="exp-img">
        </div>
        <div class="work-experience">
            <h3 class="exp-title">Work experience</h3>
            <div class="work-exp-container">
                <div class="work-exp-row">
                    <div class="exp-years">2022 - to date</div>
                    <div class="exp-job"><span>Fullstack Dev - Data Engineer</span> at Intellignos | Havas Group</div>
                </div>
                <div class="work-exp-row">
                    <div class="exp-years">2021 - to date</div>
                    <div class="exp-job"><span>Freelance Frontend Dev</span></div>
                </div>
                <div class="work-exp-row">
                    <div class="exp-years">2019 - 2021</div>
                    <div class="exp-job"><span>Judge's Clerk / Court Clerk</span> at National Courthouse</div>
                </div>
                <div class="work-exp-row">
                    <div class="exp-years">2014 - 2019</div>
                    <div class="exp-job"><span>Legal Administrative Assistant</span> at District Attorney's Office</div>
                </div>
            </div>
        </div>

    </div>
</template>

<script setup>
import { ref } from 'vue';

const getImageURL = (imageName) => {
    return new URL(`../../assets/images/${imageName}`, import.meta.url)
}


</script>
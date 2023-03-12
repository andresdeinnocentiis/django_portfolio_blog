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
        <div class="work-experience">
            <h3 class="exp-title">Academic Background</h3>
            <div class="work-exp-container">
                <div class="work-exp-row">
                    <div class="exp-years">2023 - to date</div>
                    <div class="exp-job"><span>Blockchain Developer</span> at Udemy</div>
                </div>
                <div class="work-exp-row">
                    <div class="exp-years">2022 - 2023</div>
                    <div class="exp-job"><span>Django Developer</span> at National Technological University</div>
                </div>
                <div class="work-exp-row">
                    <div class="exp-years">2021 - 2022</div>
                    <div class="exp-job"><span>Django Developer & Python specialization</span> at Inove Academy</div>
                </div>
                <div class="work-exp-row">
                    <div class="exp-years">2020 - 2021</div>
                    <div class="exp-job"><span>Frontend Developer Bootcamp</span> at Coderhouse</div>
                </div>
                <div class="work-exp-row">
                    <div class="exp-years">2020 - 2021</div>
                    <div class="exp-job"><span>Python Programmer</span> at IT Master Academy</div>
                </div>
                <div class="work-exp-row">
                    <div class="exp-years">2017 & 2019</div>
                    <div class="exp-job"><span>Russian Language</span> at Pskov State University</div>
                </div>
                <div class="work-exp-row">
                    <div class="exp-years">2014 - 2018</div>
                    <div class="exp-job"><span>French Language</span> at Alliance Française</div>
                </div>
                <div class="work-exp-row">
                    <div class="exp-years">2012 - 2018</div>
                    <div class="exp-job"><span>Lawyer</span> at University of Buenos Aires</div>
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
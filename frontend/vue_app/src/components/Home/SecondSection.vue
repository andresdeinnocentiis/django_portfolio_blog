<template>
    <div 
    class="spacer"
    :class="{'layer1-light':!isDarkMode, 'layer1-dark': isDarkMode}"></div>
    <section 
        class="home-second-section-container"
        :class="{'sec-sect-cont-dark': isDarkMode, 'sec-sect-cont-light': !isDarkMode }"
    >
        
        <h1 class="sec-sect-title" v-motion-slide-visible-right >Professional Background</h1>

        <div class="dexterities-container">
            <div 
                class="card-dex"
                v-for="dex in dexterities" 
                v-motion-slide-visible-right  
            >
                <div 
                    class="dex-img-container"
                    :class="{'dex-cont-dark': isDarkMode, 'dex-cont-light': !isDarkMode}"
                >
                    <font-awesome-icon class="dex-img" :class="{'dex-img-dark': isDarkMode, 'dex-img-light': !isDarkMode}" :icon="dex.icon" />
                </div>
                <h3 class="dex-title">{{dex.title}}</h3>
                <p class="dex-desc">{{dex.desc}}</p>
            </div>
        </div>
    </section>
</template>

<script setup>
import { useDarkModeStore } from '../../stores/darkMode';
import { storeToRefs } from 'pinia';


const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

const dexterities = [
    {id:1,title:"FullStack Developer",desc:"With a track record of delivering high quality code, well-versed on Python, Django, Django REST Framework, React.js and Vue.js I bring a diverse skillset and experience to any team or project.",icon:"fa-solid fa-layer-group"},

    {id:2,title:"Data Engineer",desc:"Specialized in Python (including numpy, pandas, dask, parallel computing, and asynchronous programming), I work seamlessly with Google Cloud Platform to deliver efficient and scalable solutions for complex data challenges.",icon:"fa-solid fa-database"},

    {id:3,title:"Backend Developer",desc:"Continuously learning and expanding my skillset to deliver efficient and scalable solutions, in my skillset repertoire can be found Python, Django, Django REST Framework, Signals, SQL, BigQuery, PostgreSQL, Postman, MVC/MVT design patterns, API development and ERD design.",icon:"fa-solid fa-network-wired"},

    {id:4,title:"Frontend Developer",desc:"Well-versed in a variety of frontend and design technologies, including React.js, Vue.js, Javascript, HTML & CSS, Adobe Photoshop, Illustrator, and Figma. My understanding of design principles allows me to effectively manage UX/UI and create engaging user experiences.",icon:"fa-solid fa-code"},

    {id:5,title:"Lawyer",desc:"As someone who used to be a lawyer, I discovered my passion for coding and transitioned into a career as a developer. My legal background has given me valuable skills in analysis, problem-solving, and attention to detail that I bring to my work as a developer.",icon:"fa-solid fa-scale-balanced"},

    {id:6,title:"Polyglot",desc:"Being Spanish my native language, I'm fluent in English (C1 level), Russian (B2 level), and French (B2 level), enabling me to effectively communicate and collaborate with individuals from diverse backgrounds and cultures.",icon:"fa-solid fa-language"},
]


</script>
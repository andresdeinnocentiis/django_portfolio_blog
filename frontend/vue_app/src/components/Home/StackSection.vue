<template>
    <section class="stack-section"
        :class="{'stack-sect-cont-dark': isDarkMode, 'stack-sect-cont-light': !isDarkMode }"
    >
        <h3 class="sec-sect-title stack__title" v-motion-slide-visible-left >My Stack</h3>
        <div class="stack__container">
            <div v-for="tec in stack" :key="tec.id" class="stack__card" v-motion-slide-visible-left >
                <font-awesome-icon 
                    class="tec-img"
                    :class="{'tec-img-dark': isDarkMode, 'tec-img-light': !isDarkMode}" 
                    :icon="tec.icon" 
                /><font-awesome-icon v-if="tec.extra" class="tec-img tec_extra" :class="{'tec-img-dark': isDarkMode, 'tec-img-light': !isDarkMode}" 
                :icon="tec.extra"  />
                <p class="tec-name">{{tec.name}}</p>
            </div>
           
        </div>
    </section>
</template>

<script setup>
import { useDarkModeStore } from '../../stores/darkMode';
import { storeToRefs } from 'pinia';

const darkModeStore = useDarkModeStore()
const { isDarkMode } = storeToRefs(darkModeStore)

const stack = [
    {id:"1", name:"Python", icon:"fa-brands fa-python"},
    {id:"2", name:"Django", icon:"fa-brands fa-dyalog", extra:"fa-solid fa-j"},
    {id:"3", name:"Django REST Framework", icon:"fa-solid fa-circle-nodes"},
    {id:"4", name:"React.js", icon:"fa-brands fa-react"},
    {id:"5", name:"Vue.js", icon:"fa-brands fa-vuejs"},
    {id:"6", name:"Javascript", icon:"fa-brands fa-square-js"},
    {id:"7", name:"HTML", icon:"fa-brands fa-html5"},
    {id:"8", name:"CSS", icon:"fa-brands fa-css3-alt"},
    {id:"9", name:"Google Cloud Platform", icon:"fa-solid fa-cloud-arrow-up"},
    {id:"10", name:"SQL", icon:"fa-solid fa-database"},
    {id:"11", name:"REST APIs", icon:"fa-solid fa-diagram-project"},
    {id:"12", name:"Git/Github", icon:"fa-brands fa-github"},
    {id:"13", name:"Solidity", icon:"fa-brands fa-ethereum"},
]
</script>
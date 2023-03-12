<template>
    <div class="about-container" id="resume">
        <DescriptionSection />
        <Suspense>
            <SkillsSection />
            <template #fallback>
                <p>Loading...</p>
            </template>
        </Suspense>
        <ExperienceSection />
    </div>
</template>

<script setup>
import { defineAsyncComponent } from 'vue';
import DescriptionSection from '../components/About/DescriptionSection.vue'
import ExperienceSection from '../components/About/ExperienceSection.vue'

// I imported it like this so that it would do a lazy loading
const SkillsSection = defineAsyncComponent(() => 
    import('../components/About/SkillsSection.vue')
)
</script>
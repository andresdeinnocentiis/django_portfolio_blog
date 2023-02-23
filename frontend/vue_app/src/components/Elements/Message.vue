<template>
    <div :class="`alert-${variant}-container`" class="alert-container">
        <p :class="`alert-${variant}-text`" clas="alert-text">{{message}}</p>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    message: String,
    variant: String,
})
</script>
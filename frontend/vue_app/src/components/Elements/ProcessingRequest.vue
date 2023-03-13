<template>
    <div class="is-sure-modal">
        <div class="is-sure-modal-container">
            <div class="modal-sure-content-container">
                <h4 class="is-sure-modal-title">{{text}}</h4>
            </div>
        </div>
    </div>
</template>


<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    text: String,
})




</script>


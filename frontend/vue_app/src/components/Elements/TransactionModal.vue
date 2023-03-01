<template>
    <div class="transaction-modal" :class="`transaction-modal-${props.variant} ${tsxHiddenClass}`">
        <div class="transaction-modal-container">
            <font-awesome-icon icon="fa-solid fa-xmark" class="close-modal-tsx" @click.prevent="toggleTsxModal"/>
            <div class="modal-tsx-content-container">
                <font-awesome-icon class="transaction-modal-icon transaction-modal-icon-success" v-if="props.success" icon="fa-regular fa-circle-check" />
                <font-awesome-icon class="transaction-modal-icon transaction-modal-icon-danger" v-else icon="fa-regular fa-circle-xmark" />
                <h4 class="transaction-modal-title">{{props.title}}</h4>
                <p class="transaction-modal-message">{{ props.message }}</p>
            </div>
        </div>
    </div>
</template>


<script setup>
import { defineProps } from 'vue';
import { storeToRefs } from 'pinia';
import { useModalStore } from '../../stores/modal';

const props = defineProps({
    variant: String,
    title: String,
    message: String,
    success: Boolean
})

const modalStore = useModalStore()
const { tsxHiddenClass } = storeToRefs(modalStore)
const { toggleTsxModal } = modalStore

</script>


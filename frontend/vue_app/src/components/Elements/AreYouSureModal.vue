<template>
    <div class="is-sure-modal" :class="sureHiddenClass">
        <div class="is-sure-modal-container">
            <font-awesome-icon icon="fa-solid fa-xmark" class="close-modal-sure" @click.prevent="toggleSureModal"/>
            <div class="modal-sure-content-container">
                <h4 class="is-sure-modal-title">Are you sure you want to {{props.action}}?</h4>
                <div class="is-sure-btns">
                    <div class="btn-no" @click.prevent="toggleSureModal">No</div>
                    <div class="btn-yes" @click.prevent="handleYes">Yes</div>
                </div>
            </div>
        </div>
    </div>
</template>


<script setup>
import { defineProps } from 'vue';
import { storeToRefs } from 'pinia';
import { useModalStore } from '../../stores/modal';

const props = defineProps({
    action: String,
    method: Function
})

const modalStore = useModalStore()
const { sureHiddenClass } = storeToRefs(modalStore)
const { toggleSureModal } = modalStore

const handleYes = () => {
    toggleSureModal()
    props.method()
}

</script>


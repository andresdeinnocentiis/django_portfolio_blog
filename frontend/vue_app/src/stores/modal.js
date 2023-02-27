import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useTechStore } from '../stores/techs';



export const useModalStore = defineStore('modal', () => {

    const isProjectModalOpen = ref(false)

    const techStore = useTechStore()
    const { getTechUsed } = techStore
    

    const hiddenClass = ref("hidden")
    
    const toggleProjectModal = () => {
        isProjectModalOpen.value = !isProjectModalOpen.value
        if (isProjectModalOpen.value) {
            hiddenClass.value = ""
            getTechUsed()
        } else {
            hiddenClass.value = "hidden"
        }

    }

    return { isProjectModalOpen, hiddenClass, toggleProjectModal }
})
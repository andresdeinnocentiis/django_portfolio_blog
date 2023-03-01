import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useTechStore } from '../stores/techs';



export const useModalStore = defineStore('modal', () => {

    const isProjectModalOpen = ref(false)
    const isEditProjectModalOpen = ref(false)
    const isTsxModalOpen = ref(false)
    const isSureModalOpen = ref(false)

    const techStore = useTechStore()
    const { getTechUsed } = techStore
    

    const hiddenClass = ref("hidden")
    const editHiddenClass = ref("hidden")
    const tsxHiddenClass = ref("hidden")
    const sureHiddenClass = ref("hidden")
    
    const toggleProjectModal = () => {
        isProjectModalOpen.value = !isProjectModalOpen.value
        if (isProjectModalOpen.value) {
            hiddenClass.value = ""
            getTechUsed()
        } else {
            hiddenClass.value = "hidden"
        }

    }
    const toggleEditProjectModal = () => {
        isEditProjectModalOpen.value = !isEditProjectModalOpen.value
        if (isEditProjectModalOpen.value) {
            editHiddenClass.value = ""
            getTechUsed()
        } else {
            editHiddenClass.value = "hidden"
        }

    }

    const toggleTsxModal = () => {
        isTsxModalOpen.value = !isTsxModalOpen.value
        if (isTsxModalOpen.value) {
            tsxHiddenClass.value = ""

        } else {
            tsxHiddenClass.value = "hidden"
        }
    }

    const toggleSureModal = () => {
        isSureModalOpen.value = !isSureModalOpen.value
        if (isSureModalOpen.value) {
            sureHiddenClass.value = ""

        } else {
            sureHiddenClass.value = "hidden"
        }
    }


    return { isProjectModalOpen, hiddenClass, toggleProjectModal, 
        isEditProjectModalOpen, editHiddenClass, toggleEditProjectModal,
        isTsxModalOpen, tsxHiddenClass, toggleTsxModal,
        isSureModalOpen, sureHiddenClass, toggleSureModal
    }
})
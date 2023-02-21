import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useNavMenuStore =  defineStore("navMenu", () => {
  
  const isMenuOpen = ref(false)

  const toggleOpenMenu = () => {
    isMenuOpen.value = !isMenuOpen.value  
  }

  return { isMenuOpen, toggleOpenMenu }
  
});
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useDarkModeStore =  defineStore("darkMode", () => {
  
  const isDarkMode = ref(
    JSON.parse(localStorage.getItem("isDarkMode")) ?? true
  )

  const toggleDarkMode = () => {
    isDarkMode.value = !isDarkMode.value  
    localStorage.setItem('isDarkMode', JSON.stringify(isDarkMode.value))
  }

  return { isDarkMode, toggleDarkMode }
  
});

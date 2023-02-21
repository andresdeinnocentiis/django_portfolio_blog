import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserLoggedStore = defineStore("userLogged", () => {
  
  const userInfo = ref(null) 

  const login = async (username, password) => {
    // Make an API request to authenticate the user
    const response = await fetch('/api/users/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    })

    if (response.ok) {
      // Update the store state with the logged in user's information
      const user = await response.json()
      userInfo.value = user
      // Save the user info to local storage
      localStorage.setItem('userInfo', JSON.stringify(user))
    } else {
        // Handle login failure
        userInfo.value = null
        // Throw an error or display an error message to the user
        throw new Error('Login failed. Please try again.')
    }
  }

  const logout = () => {
        // Clear the store state and remove the user info from local storage
        userInfo.value = null
        localStorage.removeItem('userInfo')    
    }
 
  const isUserLogged = () => {
    return !!userInfo.value // Usar doble "!!" convierte al objeto en booleano, porque si usara solo this.userInfo sería un objeto
  }
  
  return { userInfo, login, logout, isUserLogged }
});

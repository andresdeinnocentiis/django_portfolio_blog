import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getAPI } from '../axios-api';

export const useUserLoggedStore = defineStore("userLogged", () => {
  
  const userInfo = ref(null) 
  const logging = ref(false)

  const loadUserInfo = () => {
    const userInfoFromLocalStorage = localStorage.getItem('userInfo')
    if (userInfoFromLocalStorage) {
      userInfo.value = JSON.parse(userInfoFromLocalStorage)
    }
  }

  const login = async (username, password) => {
    try{
      // Make an API request to authenticate the user
      logging.value = true
      const config = {
        headers: {
          'Content-type' : 'application/json'
        }
      }

      const response = await getAPI.post('/api/users/login/',
        {'username': username, 'password': password},
        config
      )

      const user = response.data
      userInfo.value = user
      // Save the user info to local storage
      localStorage.setItem('userInfo', JSON.stringify(user))

      return true; // Login successful
       
    } catch(error) {
        
        // Handle login failure
        userInfo.value = null
        // login failed
        return false; 

    } finally {
        logging.value = false
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


  loadUserInfo()
  
  return { userInfo, login, logout, isUserLogged }
});

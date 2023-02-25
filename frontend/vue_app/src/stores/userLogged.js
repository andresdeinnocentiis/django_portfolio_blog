import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getAPI } from '../axios-api';

export const useUserLoggedStore = defineStore("userLogged", () => {
  
  const userInfo = ref(null) 
  const logging = ref(false)
  const isUserAdmin = ref(false)

  const loadUserInfo = () => {
    const userInfoFromLocalStorage = localStorage.getItem('userInfo')
    if (userInfoFromLocalStorage) {
      userInfo.value = JSON.parse(userInfoFromLocalStorage)
      isUserAdmin.value = userInfo.value.isAdmin
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

      const userData = response.data
      
      // with the default user data we get the full extended User (Profile User) 
      const profileUser = await getProfileUser(userData)

      

      // We update the state of userInfo with the data of profileUser
      userInfo.value = profileUser

      // We save the full extended User (UserProfile) in localStorage
      localStorage.setItem('userInfo', JSON.stringify(profileUser))

      isUserAdmin.value = userInfo.value.isAdmin

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

  const getProfileUser = async(user) => {

    try {
      const response = await getAPI.get(`/api/users/${user.id}/get/`, {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Bearer ${user.token}`
      }
      })
      if(response.data) {
        const userProfile = response.data[0]

        // We destructure the object so that all the keys are at the same level
        const { user, ...rest } = userProfile;
        const profileUser = { ...user, ...rest };

        return profileUser
      }
    } catch(error) {
      console.error("ERROR: ", error);
    }
  }

  const logout = () => {
        // Clear the store state and remove the user info from local storage
        userInfo.value = null
        localStorage.removeItem('userInfo') 
        isUserAdmin.value = false   
  }
 
  const isUserLogged = () => {
    return !!userInfo.value // Usar doble "!!" convierte al objeto en booleano, porque si usara solo this.userInfo sería un objeto
  }



  loadUserInfo()
  
  return { userInfo, login, logout, isUserLogged, isUserAdmin }
});

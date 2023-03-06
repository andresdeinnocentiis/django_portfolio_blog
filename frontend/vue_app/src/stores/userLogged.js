import { ref } from 'vue'
import { defineStore } from 'pinia'
import { v4 as uuidv4 } from 'uuid'; // To generate the anonymous_identifier
import { getAPI } from '../axios-api';

export const useUserLoggedStore = defineStore("userLogged", () => {
  
  const userInfo = ref(null) 
  const anonymousUserInfo = ref(null)
  const logging = ref(false)
  const isUserAdmin = ref(false)

  

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

      // We update the state of userInfo with the data 
      userInfo.value = userData
      // We save the full extended User (UserProfile) in localStorage
      localStorage.setItem('userInfo', JSON.stringify(userData))

      isUserAdmin.value = userInfo.value.isAdmin

      if (isAnonymousUserDetected()) {
        localStorage.removeItem('anonymousUserInfo');
        anonymousUserInfo.value = null; // Reset anonymous user info
      }

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
        isUserAdmin.value = false   

        // Here I reset the anonymousUserInfo if the user logged out
        if (!isUserLogged()) {
          loadUserInfo();
        }
  }
 
  const isUserLogged = () => {
    return !!userInfo.value // Usar doble "!!" convierte al objeto en booleano, porque si usara solo this.userInfo sería un objeto
  }

  const isAnonymousUserDetected = () => {
    return !!anonymousUserInfo.value
  }

  // Load userInfo or AnonymousUser
  const loadUserInfo = () => {

    const userInfoFromLocalStorage = localStorage.getItem('userInfo')

    if (userInfoFromLocalStorage) {
      console.log("USER INFO FROM LOCAL STORAGE: ", userInfoFromLocalStorage);
      userInfo.value = JSON.parse(userInfoFromLocalStorage)
      isUserAdmin.value = userInfo.value.isAdmin

    } else {

        const anonymousUserInfoFromLocalStorage = localStorage.getItem('anonymousUserInfo')

        if (!anonymousUserInfoFromLocalStorage) {

          // if the anonymous user does not exist, set it

          const newAnonymousUser = {
            username: "",
            anonymousIdentifier: generateAnonymousIdentifier(),
          }

          // Set the new Anonymous User in the local Storage:
          localStorage.setItem('anonymousUserInfo', JSON.stringify(newAnonymousUser))
    
          // Set it to the anonymousUserInfo state
          anonymousUserInfo.value = newAnonymousUser

        } else {
          // If exists set the anon user to the anonymousUserInfo state

          anonymousUserInfo.value = JSON.parse(anonymousUserInfoFromLocalStorage)
        
        }
    }
  }



  // ANONYMOUS USER ACTIONS:

  // Function to generate an anonymous_identifier
  const generateAnonymousIdentifier = () => {
    return uuidv4();
  }

  const createAnonymousUser = async (anonymousUser) => {

    try {
      const response = await getAPI.post('/api/anonymous_users/register/', anonymousUser)
      
      return true
      
    } catch (error) { 
      
        console.log(error);
        console.error(error);
        return false

    }
  }

  const getAnonymousUser = async (anonymous_identifier) => {

    try {
      const response = await getAPI.get(`/api/anonymous_users/${anonymous_identifier}/get/`)
      if (response.data) {
        const anon_user = response.data
        anonymousUserInfo.value = anon_user
        // Save the post info to local storage
        localStorage.setItem('anonymousUserInfo', JSON.stringify(anon_user))
      } else {
         // Handle failure
         // If it doesn't exist in the database, we populate his info from the localStorage (because when the user is not logged, automatically gets stored there an anon user)
         anonymousUserInfo.value = localStorage.getItem('anonymousUserInfo')
         
      }
    } catch(error) {
      console.log(error)
    }

  }

  loadUserInfo()
  
  return { userInfo, anonymousUserInfo, login, logout, isUserLogged, isUserAdmin, isAnonymousUserDetected, createAnonymousUser, getAnonymousUser }
});

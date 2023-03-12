import { ref } from 'vue'
import { defineStore, storeToRefs } from 'pinia'
import { getAPI } from '../axios-api';


export const useValidationsStore = defineStore("validationsStore", () => {
 
    const validationsList = ref(null) 
    
    const currentSkillValidation = ref(null)
    const currentStudyValidation = ref(null)

    const isSkillValidatedByUser = ref(false)
    const isStudyValidatedByUser = ref(false)

    const getValidations = async () => {

        try {
            const response = await getAPI.get('/api/validations/get/')

            if (response.data) {
                // Update the store state with the posts' information
                const validations = response.data
                validationsList.value = validations
                // Save the validations info to local storage
                localStorage.setItem('validationsList', JSON.stringify(validations))
            } else {
                // Handle failure
                validationsList.value = [{}]
                // Throw an error or display an error message to the user
                throw new Error('Failed getting the validations. Please try again.')
            }
        } catch (error) {
            console.log(error)
        }
    }



    const getUserValidationForStudy = async(studyId, user) => {
        let validationResult = {}
        let identifier

        if (user.anonymous_identifier) {
            identifier = user.anonymous_identifier

            try {
                const response = await getAPI.get(`/api/validations/study/${studyId}/anonymous_user/${identifier}/get/`, {})
                const validationArray = response.data
 
                if (validationArray.length > 0) {
                    const validationObj = validationArray[0]
                    if(validationObj.study == studyId && (validationObj.anonymous_identifier == identifier)) {
                        validationResult = validationObj
                        isStudyValidatedByUser.value = true
                        
                    } else {
                        isStudyValidatedByUser.value = false
                        
                    }
                } else {
                    validationResult = {}
                    isStudyValidatedByUser.value = false
                    
                }
                
                currentStudyValidation.value = validationResult        
            } catch(error) {
                console.log(error);
            }
        } else {

            identifier = user.id

            try {
                const response = await getAPI.get(`/api/validations/study/${studyId}/user/${identifier}/get/`, {})
                const validationArray = response.data
  
                if (validationArray.length > 0) {
                    const validationObj = validationArray[0]
                    if(validationObj.study == studyId && (validationObj.user == identifier)) {
                        validationResult = validationObj
                        isStudyValidatedByUser.value = true
                        
                    } else {
                        isStudyValidatedByUser.value = false
                        
                    }
                } else {
                    validationResult = {}
                    isStudyValidatedByUser.value = false
                    
                    
                }
                
                currentStudyValidation.value = validationResult       
                
            } catch(error) {
                console.log(error);
            }
        }
    }

    const getUserValidationForSkill = async(skillId, user) => {
        let validationResult = {}
        let identifier

        if (user.anonymous_identifier) {
            identifier = user.anonymous_identifier

            try {
                const response = await getAPI.get(`/api/validations/technology/${skillId}/anonymous_user/${identifier}/get/`, {})
                const validationArray = response.data
 
                if (validationArray.length > 0) {
                    const validationObj = validationArray[0]
                    if(validationObj.technology == skillId && (validationObj.anonymous_identifier == identifier)) {
                        validationResult = validationObj
                        isSkillValidatedByUser.value = true
                        
                    } else {
                        isSkillValidatedByUser.value = false
                        
                    }
                } else {
                    validationResult = {}
                    isSkillValidatedByUser.value = false
                    
                }
                
                currentSkillValidation.value = validationResult        
            } catch(error) {
                console.log(error);
            }
        } else {

            identifier = user.id

            try {
                const response = await getAPI.get(`/api/validations/technology/${skillId}/user/${identifier}/get/`, {})
                const validationArray = response.data
  
                if (validationArray.length > 0) {
                    const validationObj = validationArray[0]
                    if(validationObj.technology == skillId && (validationObj.user == identifier)) {
                        validationResult = validationObj
                        isSkillValidatedByUser.value = true
                        
                    } else {
                        isSkillValidatedByUser.value = false
                        
                    }
                } else {
                    validationResult = {}
                    isSkillValidatedByUser.value = false
                    
                    
                }
                
                currentSkillValidation.value = validationResult       
                
            } catch(error) {
                console.log(error);
            }
        }
    }

    const postValidation = async (validation) => {
        try {
            const response = await getAPI.post('/api/validations/post/', validation, {
            headers: {
                'Content-Type': 'application/json',
            }
            });

            if (response.status === 201) {
                // Now we update the validations 
                getValidations()

            }

            return true
        } catch (error) { 
            console.log(error);
            return false
        }
    }
    
    const deleteValidation = async (validationId) => {
        try {
            const response = await getAPI.delete(`/api/validations/${validationId}/delete/`, {
                headers: {
                    'Content-Type': 'application/json',
                }
            })

            
            // Now we update the validations:
            getValidations()

            

            return true
        } catch (error) {
            console.log(error);
 
            return false
        }
    }

    return { validationsList, getValidations, postValidation, deleteValidation, 
        getUserValidationForStudy, currentStudyValidation, isStudyValidatedByUser,
        getUserValidationForSkill, currentSkillValidation, isSkillValidatedByUser, 
    }
})

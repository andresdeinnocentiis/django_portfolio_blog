import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getAPI } from '../axios-api';

export const useStudiesStore = defineStore("studiesStore", () => {
  
    const listStudies = ref([]) 

    const getStudies = async () => {

        try {
            const response = await getAPI.get('/api/studies/get/')

            if (response.data) {
            // Update the store state with the posts' information
                const tech = response.data
                listStudies.value = tech
            } else {
                // Handle failure
                listStudies.value = []
                // Throw an error or display an error message to the user
                throw new Error('Failed getting the studies. Please try again.')
            }

        } catch(error) { 
            console.error("ERROR: ", error);
        } 

    }
  
  return { listStudies, getStudies }
});

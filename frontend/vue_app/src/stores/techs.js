import { ref } from 'vue'
import { defineStore } from 'pinia'
import { getAPI } from '../axios-api';

export const useTechStore = defineStore("getTech", () => {
  
    const listTech = ref([]) 

    const getTechUsed = async () => {

        try {
            const response = await getAPI.get('/api/technologies/get/')

            if (response.data) {
            // Update the store state with the posts' information
                const tech = response.data
                listTech.value = tech
            } else {
                // Handle failure
                listTech.value = []
                // Throw an error or display an error message to the user
                throw new Error('Failed getting the techs. Please try again.')
            }

        } catch(error) { 
            console.error("ERROR: ", error);
        } 

    }
  
  return { listTech, getTechUsed }
});

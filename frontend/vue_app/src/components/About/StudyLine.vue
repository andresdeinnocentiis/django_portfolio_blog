<template>
    <tr class="tech-line-container">
        <td>{{study.name}}</td>
        <td class="study-cell-desc">{{study.description}}</td>
        <td class="table-num-validations">{{study.validations}}</td>
        <td class="validate-btn-td validate-btn-col">
            <button class="validate-btn" @click.prevent="handleValidateClick(study.id, 'study')">{{isValidated ? 'Remove Validation' : 'Validate Knowledge'}}</button>
        </td>
    </tr>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { ref } from 'vue';
import { useStudiesStore } from '../../stores/studies';
import { useValidationsStore } from '../../stores/validations';
import { useUserLoggedStore } from '../../stores/userLogged';


const props = defineProps({
    study: {
        type: Object,
        required: true
    }
})



const studiesStore = useStudiesStore()
const { listStudies } = storeToRefs(studiesStore)
const { getStudies } = studiesStore

const validationsStore = useValidationsStore()
const { postValidation, deleteValidation, getUserValidationForSkill, getUserValidationForStudy } = validationsStore
const { currentStudyValidation, currentSkillValidation, isSkillValidatedByUser, isStudyValidatedByUser } = storeToRefs(validationsStore)

const userLoggedStore = useUserLoggedStore()
const { userInfo, anonymousUserInfo } = storeToRefs(userLoggedStore)

const isValidated = ref(false)


const handleValidateClick = async (itemId, itemType) => {

    // Create the Validation Object that would be sent if the request is POST
    const validationObj = {
        user: userInfo.value ? userInfo.value.id : null,
        anonymous_identifier: anonymousUserInfo.value ? anonymousUserInfo.value.anonymous_identifier : null,
        technology: itemType === "technology" ? itemId : null,
        study: itemType === "study" ? itemId : null
    }
    // If it's a logged user:
    if(userInfo.value) {
        try {
            // If the study is already validated and the user clicked it, then it has to be deleted
            if (itemType === "study") {
                await getUserValidationForStudy(itemId, userInfo.value)
                if (isStudyValidatedByUser.value) {
                    await deleteValidation(currentStudyValidation.value.id)
                    // Update the validation to see the changes in real time
                    await getUserValidationForStudy(itemId, userInfo.value)
                    isValidated.value = false
                    props.study.validations--

                // If the study is not yet validated and the user clicked it, then it has to be created
                } else {
                    await postValidation(validationObj)
                    // Update the validation to see the changes in real time
                    await getUserValidationForStudy(itemId, userInfo.value)
                    isValidated.value = true
                    props.study.validations++
                }
            } else if (itemType === "technology") {
                await getUserValidationForSkill(itemId, userInfo.value)
                if (isSkillValidatedByUser.value) {
                    await deleteValidation(currentSkillValidation.value.id)
                    // Update the validation to see the changes in real time
                    await getUserValidationForSkill(itemId, userInfo.value)
                    isValidated.value = false
                    props.tech.validations--

                // If the technology is not yet validated and the user clicked it, then it has to be created
                } else {
                    await postValidation(validationObj)
                    // Update the validation to see the changes in real time
                    await getUserValidationForSkill(itemId, userInfo.value)
                    isValidated.value = true
                    props.tech.validations++
                }
            }
        } catch(error) {
            console.error(error);
        }
    // If it's an unregistered user:    
    } else {
        try {
            // If the study is already validated and the user clicked it, then it has to be deleted
            if (itemType === "study") {
                await getUserValidationForStudy(itemId, anonymousUserInfo.value)
                if (isStudyValidatedByUser.value) {
                    await deleteValidation(currentStudyValidation.value.id)
                    // Update the validation to see the changes in real time
                    await getUserValidationForStudy(itemId, anonymousUserInfo.value)
                    isValidated.value = false
                    props.study.validations--
                // If the study is not yet validated and the user clicked it, then it has to be created
                } else {
                    await postValidation(validationObj)
                    // Update the validation to see the changes in real time
                    await getUserValidationForStudy(itemId, anonymousUserInfo.value)
                    isValidated.value = true
                    props.study.validations++
                } 
            } else if (itemType === "technology") {
                await getUserValidationForSkill(itemId, anonymousUserInfo.value)
                if (isSkillValidatedByUser.value) {
                    await deleteValidation(currentSkillValidation.value.id)
                    // Update the validation to see the changes in real time
                    await getUserValidationForSkill(itemId, anonymousUserInfo.value)
                    isValidated.value = false
                    props.tech.validations--
                // If the tech is not yet validated and the user clicked it, then it has to be created
                } else {
                    await postValidation(validationObj)
                    // Update the validation to see the changes in real time
                    await getUserValidationForSkill(itemId, anonymousUserInfo.value)
                    isValidated.value = true
                    props.tech.validations++
                } 
            }
        } catch(error) {
            console.error(error);
        }
        
    }

}


getStudies()


if (userInfo.value) {
    await getUserValidationForStudy(props.study.id, userInfo.value)
    isValidated.value = isStudyValidatedByUser.value

} else {
    await getUserValidationForStudy(props.study.id, anonymousUserInfo.value)
    isValidated.value = isStudyValidatedByUser.value
}

</script>
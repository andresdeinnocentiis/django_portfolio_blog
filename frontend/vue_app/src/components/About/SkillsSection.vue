<template>
    <div class="skills-section-container">
        <h3>Skills</h3>
        
        <table class="about-techs-container">
            <thead class="head-row">
                <tr>
                    <th>Skill</th>
                    <th>Validations</th>
                    <th class="validate-header validate-btn-col">Validate my skills!</th>
                </tr>
            </thead>
            <tbody>
                <SkillLine 
                    v-for="tech in listTech"
                    :tech="tech"
                />
            </tbody>
        </table>

        <h3>Studies</h3>
        
        <table class="about-techs-container about-studies-container">
            <thead>
                <tr>
                    <th>Study</th>
                    <th>Description</th>
                    <th>Validations</th>
                    <th class="validate-header validate-btn-col">Validate my studies!</th>
                </tr>
            </thead>
            <tbody>
                <StudyLine 
                    v-for="study in listStudies"
                    :study="study"
                />
            </tbody>
        </table>
    </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { ref } from 'vue';
import { useTechStore } from '../../stores/techs';
import { useStudiesStore } from '../../stores/studies';
import { useValidationsStore } from '../../stores/validations';
import { useUserLoggedStore } from '../../stores/userLogged';
import SkillLine from './SkillLine.vue';
import StudyLine from './StudyLine.vue';

const techStore = useTechStore()
const { listTech } = storeToRefs(techStore)
const { getTechUsed } = techStore

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

    // Create the Like Object that would be sent if the request is POST
    const validationObj = {
        user: userInfo.value ? userInfo.value.id : null,
        anonymous_identifier: anonymousUserInfo.value ? anonymousUserInfo.value.anonymous_identifier : null,
        technology: itemType === "technology" ? itemId : null,
        study: itemType === "study" ? itemId : null
    }
    // If it's a logged user:
    if(userInfo.value) {
        try {
            // If the comment is already liked and the user clicked it, then it has to be deleted
            if (itemType === "study") {
                await getUserValidationForStudy(itemId, userInfo.value)
                if (isStudyValidatedByUser.value) {
                    await deleteValidation(currentStudyValidation.value.id)
                    // Update the like to see the changes in real time
                    await getUserValidationForStudy(commentId, userInfo.value)
                    isValidated.value = false
                    props.comment.likes--

                // If the comment is not yet liked and the user clicked it, then it has to be created
                } else {
                    await postValidation(validationObj)
                    // Update the like to see the changes in real time
                    await getUserLikeForComment(commentId, userInfo.value)
                    isValidated.value = true
                    props.comment.likes++
                }
            } else if (itemType === "technology") {
                await getUserValidationForSkill(itemId, userInfo.value)
                if (isSkillValidatedByUser.value) {
                    await deleteValidation(currentSkillValidation.value.id)
                    // Update the like to see the changes in real time
                    await getUserValidationForSkill(itemId, userInfo.value)
                    isValidated.value = false
                    //props.comment.likes--

                // If the comment is not yet liked and the user clicked it, then it has to be created
                } else {
                    await postValidation(validationObj)
                    // Update the like to see the changes in real time
                    await getUserValidationForSkill(itemId, userInfo.value)
                    isValidated.value = true
                    //props.comment.likes++
                }
            }
        } catch(error) {
            console.error(error);
        }
    // If it's an unregistered user:    
    } else {
        try {
            // If the comment is already liked and the user clicked it, then it has to be deleted
            if (itemType === "study") {
                if (isStudyValidatedByUser.value) {
                    await deleteValidation(currentCommentLike.value.id)
                    // Update the like to see the changes in real time
                    await getUserValidationForStudy(itemId, anonymousUserInfo.value)
                    isValidated.value = false
                    //props.comment.likes--
                // If the comment is not yet liked and the user clicked it, then it has to be created
                } else {
                    await postValidation(validationObj)
                    // Update the like to see the changes in real time
                    await getUserValidationForStudy(itemId, anonymousUserInfo.value)
                    isValidated.value = true
                    //props.comment.likes++
                } 
            } else if (itemType === "technology") {
                if (isSkillValidatedByUser.value) {
                    await deleteValidation(currentCommentLike.value.id)
                    // Update the like to see the changes in real time
                    await getUserValidationForSkill(itemId, anonymousUserInfo.value)
                    isValidated.value = false
                    //props.comment.likes--
                // If the comment is not yet liked and the user clicked it, then it has to be created
                } else {
                    await postValidation(validationObj)
                    // Update the like to see the changes in real time
                    await getUserValidationForSkill(itemId, anonymousUserInfo.value)
                    isValidated.value = true
                    //props.comment.likes++
                } 
            }
        } catch(error) {
            console.error(error);
        }
        
    }

}


getTechUsed()
getStudies()

</script>
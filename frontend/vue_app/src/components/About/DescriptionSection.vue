<template>
    <div class="desc-section-container">
        <h1 class="about-title">About</h1>
        <p class="about-short-desc">I'm Andres De Innocentiis, a Fullstack developer from Argentina with a passion for languages, tennis and acquiring new skills. I'm highly adaptable to change and love taking on new challenges.</p>
        <div class="about-full-desc-container">
            <p class="about-full-desc">After beginning my career as a lawyer, I discovered my passion for coding and transitioned into a career as a developer. I specialize in Python and have experience working with a variety of technologies both front and back end, which I have acquired through formal studies at different institutions, self-study and a lot of practice.</p> 
            <p>My skillset includes Python, Django, Django REST Framework, SQL, BigQuery, PostgreSQL, Google Cloud Platform, Postman, MVC/MVT design patterns, API development, ERD design, React.js, Vue.js, JavaScript, HTML, and CSS.</p>
            <p>Currently, I'm working as a Fullstack Developer -using Django and Vue.js- and a Data Engineer -with Python- at Intellignos | Havas Group.</p>
            <p class="about-email">If you're interested in learning more about my experience, please feel free to contact me at <span>andresdeinnocentiis@gmail.com</span></p>
            
            <p class="download-resume">Feel free to download my resume by clicking <span class="click-here" @click="exportToPDF">here</span>.</p>
        </div>
    </div>
</template>

<script setup>
import html2pdf from "html2pdf.js";

const exportToPDF = () => {
    html2pdf(document.getElementById("resume"), {
			margin: 1,
  			filename: "Andres-De-Innocentiis-Fullstack-Developer-Resume.pdf",
            jsPDF: { unit: 'in', format: 'letter', orientation: 'landscape' }
			});
}
</script>
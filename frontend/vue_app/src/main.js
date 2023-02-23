import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { MotionPlugin } from '@vueuse/motion'

import App from './App.vue'
import router from './router'

// FONTAWESOME IMPORTS:
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faPowerOff, faLayerGroup, faCode, faDatabase, faNetworkWired, faScaleBalanced, faLanguage, faCircleNodes, faCloudArrowUp, faDiagramProject, faJ} from '@fortawesome/free-solid-svg-icons'
import { faSun, faMoon, faEnvelope } from '@fortawesome/free-regular-svg-icons'
import { faLinkedin, faInstagram, faGithub, faPython, faEthereum, faHtml5, faCss3Alt, faDyalog, faReact, faVuejs, faSquareJs} from '@fortawesome/free-brands-svg-icons'

/* add icons to the library */
library.add(faPowerOff, faSun, faMoon, faLayerGroup, faCode, faDatabase, faNetworkWired, faScaleBalanced, faLanguage, faEnvelope, faLinkedin, faInstagram, faGithub, faPython, faEthereum, faHtml5, faCss3Alt, faDyalog, faReact, faVuejs, faSquareJs, faCircleNodes, faCloudArrowUp, faDiagramProject, faJ)

// END OF FONTAWESOME IMPORTS


const app = createApp(App)
const pinia = createPinia()


app.use(pinia)
app.use(router)
app.use(MotionPlugin)

/* Add font awesome icon component */
.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// FONTAWESOME IMPORTS:
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faPowerOff} from '@fortawesome/free-solid-svg-icons'
import { faSun, faMoon } from '@fortawesome/free-regular-svg-icons'

/* add icons to the library */
library.add(faPowerOff, faSun, faMoon)

// END OF FONTAWESOME IMPORTS


const app = createApp(App)
const pinia = createPinia()


app.use(pinia)
app.use(router)

/* Add font awesome icon component */
.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')

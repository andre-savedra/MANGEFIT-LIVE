import './assets/style/global.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config';


import App from './App.vue'
import router from './router'
import piniaPlugin from "pinia-plugin-persistedstate";

import Aura from '@primevue/themes/aura';
import Menubar from 'primevue/menubar';


const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPlugin)



app.use(pinia)
app.use(router)

app.use(PrimeVue,{
    theme: {
        preset: Aura
    }
});
app.component('Menubar', Menubar);


app.mount('#app')

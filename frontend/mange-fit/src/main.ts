import './assets/style/global.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config';


import App from './App.vue'
import router from './router'
import piniaPlugin from "pinia-plugin-persistedstate";

import Menubar from 'primevue/menubar';
import TabMenu  from 'primevue/tabmenu';
import Checkbox  from 'primevue/checkbox';

const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPlugin)



app.use(pinia)
app.use(router)

app.use(PrimeVue);
app.component('Menubar', Menubar);
app.component('TabMenu', TabMenu);
app.component('Checkbox', Checkbox);


app.mount('#app')

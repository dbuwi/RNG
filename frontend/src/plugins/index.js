/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import router from '../router'

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

export function registerPlugins (app) {
  app
    .use(vuetify)
    .use(router)
    .use(pinia)
}

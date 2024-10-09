import Vue from 'vue'
import App from './App'
import router from './router'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBleJxSr7tqU-007mt9S9EB-FEVSKUt854', // process.env.VUE_APP_API_KEY,
    libraries: 'places,geometry'
  }
})

/* eslint-disable*/
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

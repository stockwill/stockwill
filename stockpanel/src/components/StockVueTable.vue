<template>
  <vuetable ref="vuetable"
  :fields="fields"
  :api-mode="false"
  :data-manager="dataManager"
  >
  </vuetable>
</template>

<script>
import Vuetable from 'vuetable-2'
// Read static assets
// https://vuejs-templates.github.io/webpack/static.html#getting-asset-paths-in-javascript
// https://forum.vuejs.org/t/load-static-json-in-webpack-project/17011
// This can be improved since the JSON is compiled during webpacking
import twstockData from '../assets/twstock.json'
import lodash from 'lodash'
import FieldsDef from './FieldsDef.js'
import stock from './stock.js'

export default {
  components: {
    Vuetable
  },
  data () {
    return {
      fields: FieldsDef,
      data: []
    }
  },
  methods: {
    // See: https://www.vuetable.com/guide/api-vs-data-mode.html#data-mode
    dataManager (sortOrder, pagination) {
      let local = twstockData
      local = stock.computeData(local)

      if (sortOrder.length > 0) {
        local = lodash.orderBy(
          local,
          sortOrder[0].sortField,
          sortOrder[0].direction
        )
      }

      return {
        // data: twstockData
        data: local
      }
    }
  }
}
</script>

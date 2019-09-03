<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <StockVueTable/>
  </div>
</template>

<script>
import StockVueTable from './components/StockVueTable.vue'

export default {
  name: 'App',
  components: {
    StockVueTable
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

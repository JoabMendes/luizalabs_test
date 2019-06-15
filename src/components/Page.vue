<template>
  <div id="page">
      <b-container>
          <b-row>
              <b-col cols="12">
                  <h2>Other page</h2>
              </b-col>
          </b-row>
      </b-container>
  </div>
</template>

<script>

  import axios from 'axios';

  export default {
    name: 'Page',
    data() {
      return {
        loading: true,
      }
    },
    mounted() {
    },
    methods: {
    }
  }
</script>

<style lang="scss">


</style>

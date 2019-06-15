<template>
  <div id="index">
      <b-container>
          <b-row>
              <b-col cols="12">
                  <h2>Index page</h2>
              </b-col>
          </b-row>
      </b-container>
  </div>
</template>

<script>

  import axios from 'axios';

  export default {
    name: 'Index',
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

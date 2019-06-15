<template>
  <div id="app">
    <div id="header">
      <b-container fluid>
        <b-navbar toggleable="md" type="light" variant="light">
          <b-navbar-brand href="#/">NavBar</b-navbar-brand>
          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
          <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
              <b-nav-item href="#/page">Link</b-nav-item>
              <b-nav-item href="#/page" disabled>Disabled</b-nav-item>
            </b-navbar-nav>
            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
              <b-nav-item href="#/page">Link</b-nav-item>
              <b-nav-item href="#/page">Link</b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>
      </b-container>
    </div>
    <div id="content">
      <transition name="fade">
        <router-view></router-view>
      </transition>
    </div>
    <div id="footer">

    </div>
  </div>
</template>

<script>

  import axios from 'axios';

  export default {
    name: 'App',
    data() {
      return {
        loading: true,
      }
    },
    mounted() {
    },
    methods: {}
  }
</script>

<style lang="scss">

  #app {
    font-family: 'ABeeZee', sans-serif !important;
    letter-spacing: 2px;
    .navbar {
      height: 90px;
      #nav_collapse {
        background-color: #f8f9fa !important;
      }
    }
  }

  .fade-enter-active, .fade-leave-active {
    transition-property: opacity;
    transition-duration: .25s;
  }

  .fade-enter-active {
    transition-delay: .25s;
  }

  .fade-enter, .fade-leave-active {
    opacity: 0
  }

</style>

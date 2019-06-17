<template>
    <div id="app">
        <div id="header">
            <b-navbar toggleable="md" type="light" variant="light">
                <b-container>
                    <b-navbar-brand href="#/" id="title">
                        Luiza<span id="title-highlight">labs</span> Employee Manager
                    </b-navbar-brand>
                </b-container>
            </b-navbar>
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

    export default {
        name: 'App',
    }

</script>

<style lang="scss">

    // Main colors
    $white: #fff;
    $luizaLabsBlue: #396EAF;
    $black: #201A16;

    #app {
        font-family: 'ABeeZee', sans-serif !important;
        letter-spacing: 1px;

        .navbar {
            height: 90px;
            background-color: $luizaLabsBlue !important;
            margin-bottom: 20px !important;

            #title {
                font-family: 'Ubuntu', sans-serif;
                color: $white;
                font-weight: bold;
                letter-spacing: 0.1px;
                #title-highlight {
                    font-weight: normal;
                }
                // padding-left: 5% !important;
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

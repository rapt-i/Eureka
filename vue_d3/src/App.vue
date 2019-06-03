<template>
    <div id="app">
        <!--        <img src="./assets/logo.png">-->
        <!--        <d3_line_chart></d3_line_chart>-->
        <aircraft></aircraft>
        <!--        <router-view/>-->
    </div>
</template>

<script>
    import D3_line_chart from "@/components/d3_line_chart";
    import aircraft from "@/components/aircraft";

    export default {
        name: 'App',
        components: {
            D3_line_chart,
            aircraft
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

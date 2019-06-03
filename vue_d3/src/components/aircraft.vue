<template>
    <div>
        <h1>{{name}}</h1>
        <label>
            <select v-model="id">
                <option value="">飛行機を選んで</option>
                <option v-bind:value="aircraft.id" v-for="aircraft in aircraftList">
                    {{ aircraft.name }}
                </option>
            </select>
        </label>
        <button v-on:click="setAircraft">SET</button>
        {{eMsg}}
    </div>
</template>

<script>
    import * as axios from 'axios';

    export default {
        name: "aircraft",
        data() {
            return {
                aircraftList: [],
                id: null,
                name: null,
                eMsg: '',
            }
        },
        mounted() {
            try {
                axios
                    .get('http://127.0.0.1:8000/api/v1/aircraft/')
                    .then(response => {
                        if (response.data) {
                            for (let i = 0; i < response.data.length; i++) {
                                this.aircraftList.push(
                                    {
                                        name: response.data[i].name,
                                        id: response.data[i].id
                                    }
                                );
                            }
                        }
                        this.name = this.aircraftList[0].name;
                    });
            } catch (e) {
                this.eMsg = e
            }
        },
        methods: {
            setAircraft: function () {
                this.name = this.aircraftList[this.id - 1].name;
            }
        }
    }
</script>

<style scoped>

</style>

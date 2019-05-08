new Vue({
    el: '#flight_data',
    data() {
        return {
            data: [],
            speed: [],
        }
    },
    filters: {
        currencydecimal(value) {
            return value.toFixed(2)
        }
    },
    mounted() {
        axios
            .get('/api/v1/flightdata/')
            .then(response => {
                if (response.data) {
                    for (let i = 0; i < response.data.length; i++) {
                        this.speed.push(response.data[i].speed)
                    }
                }
            })
    }
});
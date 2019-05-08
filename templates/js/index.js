let api = {
    v1: {
        aircraft: function () {
            return '/api/v1/aircraft/'
        },
        tftype: function () {
            return '/api/v1/tftype/'
        },
        flighttype: function () {
            return '/api/v1/flighttype/'
        },
        flightdata: function () {
            return '/api/v1/flightdata/'
        },
    }
};


let aircraft = new Vue({
    el: "#aircraft",
    data() {
        return {
            id: '',
            name: '',
        }
    },
    mounted() {
        axios
            .get(api.v1.aircraft())
            .then(response => {
                if (response.data) {
                    for (let i = 0; i < response.data.length; i++) {
                        this.id = this.id + response.data[i].id;
                        this.name = this.name + response.data[i].name;
                    }
                }
            })
    }
});

let tf_data = new Vue({
    el: "#tf_data",
    data() {
        return {
            info: null
        }
    },
    mounted() {
        axios
            .get(api.v1.tftype())
            .then(response => {
                this.info = response.data;
            })
    }
});

let fligth_data = new Vue({
    el: "#flight_data",
    data() {
        return {
            time: [],
            height: [],
            speed: [],
            angle: [],
            rotation: []
        }
    },
    mounted() {
        axios
            .get(api.v1.flightdata())
            .then(response => {
                for (let i = 0; i < response.data.length; i++) {
                    this.time.push(response.data[i].time);
                    this.height.push(response.data[i].height);
                    this.speed.push(response.data[i].speed);
                    this.angle.push(response.data[i].steering_angle);
                    this.rotation.push(response.data[i].rotation);
                }
            });
    }
});


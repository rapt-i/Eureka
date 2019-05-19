import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import D3_chart from '@/components/d3_line_chart'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            name: 'HelloWorld',
            component: HelloWorld
        },
        {
            path: '/chart',
            name: "D3-chart",
            component: D3_chart
        }
    ]
})

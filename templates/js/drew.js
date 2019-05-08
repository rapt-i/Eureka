function drewGraph() {
    let dataset = [];
    for (let i = 0; i < fligth_data.height.length; i++) {
        dataset.push([fligth_data.time[i], fligth_data.height[i]]);
    }
    var min = d3.min(dataset, function (d) {
        return d;
    });
    var max = d3.max(dataset, function (d) {
        return d[1];
    });

// 图表的宽度和高度
    var width = 600;
    var height = 600;
// 预留给轴线的距离
    var padding = {top: 50, right: 50, bottom: 50, left: 50};

    var xScale = d3.scaleLinear()
        .domain([1, 12])
        .range([0, width - padding.left - padding.right]);
    var yScale = d3.scaleLinear()
        .domain([0, max])
        .range([height - padding.top - padding.bottom, 0]);

    var svg = d3.select('#height')
        .append('svg')
        .attr('width', width + 'px')
        .attr('height', height + 'px');
    var xAxis = d3.axisBottom()
        .scale(xScale);
    var yAxis = d3.axisLeft()
        .scale(yScale);

    svg.append('g')
        .attr('class', 'axis')
        .attr('transform', 'translate(' + padding.left + ',' + (height - padding.bottom) + ')')
        .call(xAxis);
    svg.append('g')
        .attr('class', 'axis')
        .attr('transform', 'translate(' + padding.left + ',' + padding.top + ')')
        .call(yAxis);


    var linePath = d3.line()
        .x(function (d) {
            return xScale(d[0])
        })
        .y(function (d) {
            return yScale(d[1])
        });
    svg.append('g')
        .append('path')
        .attr('class', 'line-path')
        .attr('transform', 'translate(' + padding.left + ',' + padding.top + ')')
        .attr('d', linePath(dataset))   // <-- 注目
        .attr('fill', 'none')
        .attr('stroke-width', 3)
        .attr('stroke', 'green');

    svg.append('g')
        .selectAll('circle')
        .data(dataset)
        .enter()
        .append('circle')
        .attr('r', 5)
        .attr('transform', function (d) {
            return 'translate(' + (xScale(d[0]) + padding.left) + ',' + (yScale(d[1]) + padding.top) + ')'
        })
        .attr('fill', 'green');
};
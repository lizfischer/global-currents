var data = ["green"];


 d3.select('#chart').selectAll('div')
        .data(data)
        .enter().append('div')
        .classed('item', true)
        .text(function (d) {
            return d;
        })
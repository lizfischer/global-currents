var data = [];
d3.json(json_result, function(d) {
    for (key in d) {
        console.log(key);
        data.push(d[key].color);
    }

    d3.select('#chart').selectAll('div')
        .data(data)
        .enter().append('div')
        .classed('item', true)
        .text(function (d) {
            return d.color;
        })

});


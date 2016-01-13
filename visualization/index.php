<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>D3 Test</title>
        <script type="text/javascript" src="d3/d3.js"></script>
    </head>
    <body>
        <?php
        //include_once("utils.php");
        //echo getJSON("SELECT Century, COUNT(MS_Number) FROM Date GROUP BY Century");
        ?>

        <script type="text/javascript">
            var data = [
                {
                    "cent":9,
                    "red":50,
                    "blue":47,
                    "green":12
                },
                {
                    "red":
                }];

            d3.select("body").append("div")
                .attr("class", "chart");

            var chart = d3.select(".chart");
            var bar = chart.selectAll("div");
            var barUpdate = bar.data(data);
            var barEnter = barUpdate.enter().append("div");
            barEnter.style("width", function(d) { return d / 2 + "px"; });
            barEnter.style("background-color", "red");
            barEnter.text(function(d) { return d; });
        </script>

    </body>
</html>
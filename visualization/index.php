<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>D3 Test</title>

        <link rel="stylesheet" href="_/base.css">
        <link rel="stylesheet" href="_/style.css"

    </head>
    <body>
        <?php
        include_once("mysqlConfig.php");
        try {
            //RUN QUERY
            $query =  "SELECT primary_color as color, count(*) as count FROM enlarged_capital WHERE iserror=0 GROUP BY primary_color";
            $result = $db->query($query);

            //FORMAT RESULT
            $data = array();
            for ($x = 0; $x < mysqli_num_rows($result); $x++) {
                $data[] = mysqli_fetch_assoc($result);
            }
            $json = json_encode($data);
        } catch (Exception $e){
            echo $e->getMessage();
        }
        ?>

        <script type="text/javascript">
            var json_result = <?php echo $json; ?>;
        </script>

        <div id="container">
            <h2>D3 graphic</h2>
            <section id="chart">

            </section>




<!--
            <svg width="600" height="400"
                    style="background: #93A1A1">
                <rect x="250" y="150" width="100" height="100"
                        style="fill: #C61C6F" />
                <circle cx="300"  cy="200" r="50"
                        style="fill: #840043"/>
                <text x="10" y="390" font-family="sans-serif"
                        font-size="25" style="fill: white"> SVG Graphics </text>

                <g id="triangle">
                    <polyline points="10 35, 30 10, 50 35"
                        style="fill: #595AB7"/>
                </g>
                
                <use xlink:href="#triangle" x="30" y="0"/>
            </svg>-->
        </div>


        <script type="text/javascript" src="_/d3.js"></script>
        <script type="text/javascript" src="_/script.js"></script>
    </body>
</html>
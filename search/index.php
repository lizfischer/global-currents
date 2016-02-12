<!DOCTYPE html>
<html>
    <head>
        <title>Search</title>
        <script type="text/javascript" src="jquery.js"></script>
        <script type="text/javascript" src="modules.js"></script>
    </head>
    <body>
        <div id="search">
            <form action="index.php" method="get">
                <label>Please choose a feature for which to search.</label>
                <select id="feature-type">
                    <script>
                        for (var i in features){
                            var f = features[i];
                            document.write("<option value='"+ f.shorthand)+"'>"+ f.human +"</option>")
                        }
                    </script>
                </select>
                <input type="button" value="Go" class="add" id="add" />
            </form>
            <form action="index.php" method="get">
                <fieldset id="feature-search-wrapper">
                </fieldset>
                <input class="button-primary" type="submit" name="submit" value="Search">
            </form>
        </div>
    </body>
</html>
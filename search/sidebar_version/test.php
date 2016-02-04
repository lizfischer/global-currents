<!DOCTYPE html>
<html lang="en">
<head>

    <!-- Basic Page Needs
    –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <meta charset="utf-8">
    <title>Global Currents | Data Viewer</title>
    <meta name="description" content="">
    <meta name="author" content="Liz Fischer">

    <!-- Mobile Specific Metas
    –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- FONT
    –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <link href="//fonts.googleapis.com/css?family=Raleway:400,300,600" rel="stylesheet" type="text/css">

    <!-- CSS
    –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <link rel="stylesheet" href="css/normalize.css">
    <link rel="stylesheet" href="css/skeleton.css">
    <link rel="stylesheet" href="css/gc-test.css">

    <!-- JS
      ----------------------------------------- -->
    <script type="text/javascript" src="javascript/jquery.js"></script>
    <script type="text/javascript" src="javascript/nav.js"></script>

    <!-- Favicon
    –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <link rel="icon" type="image/png" href="images/favicon.png">

</head>
<body>

<?php include_once vars.php ?>

<!-- Primary Page Layout
–––––––––––––––––––––––––––––––––––––––––––––––––– -->
<div id="top-bar"></div>
<div class="side-bar">
    <ul class="nav">
        <form action="index.php" method="get">
            <fieldset id="feature-search-wrapper">
                <div class="option">
                    <p class="ms-field"> Manuscript:
                        <select name="manuscript">
                            <option value=''></option>
                            <?php
                            foreach ($ms_number as $n){
                                echo "<option value='".$n."''>".$n."</option>";
                            }
                            ?>
                        </select></p>
                    <p class="folio-field"> Folio:
                        <input type="text" name="folio-num"> <br>
                        <input type="radio" name="folio-rvp" value="R">R
                        <input type="radio" name="folio-rvp" value="V">V
                        <input type="radio" name="folio-rvp" value="P"> Page
                    </p>
                    <p class="feature-field">
                        Feature:
                        <select name='feature-select'>
                            <option value = 'ln'>Litterae Notabiliores</option>
                            <option value = 'ec'>Enlarged Capitals</option>
                            <option value = 'rubric'>Rubrics</option>
                        </select><br>
                    </p>
                    <p class="p-color-field">
                        Primary Color
                        <select name='primary-color'>
                            <?php

                            ?>
                        </select>
                    </p>
                    <p class="s-color-field">
                        Secondary Color
                        <select name='secondary-color'>
                            <?php

                            ?>
                        </select>
                    </p>

                </div>
            </fieldset>

            <input type="button" value="Add a feature" class="add" id="add" />
            <input class="button-primary" type="submit" name="submit" value="Search">
        </form>
    </ul>
</div>
<div class="page-wrapper">
    <div class="row">
        <div class="ten columns content">
        </div>
    </div>
</div>


<?php
// Disconnect from database
$db->close();
?>

<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
</body>
</html>
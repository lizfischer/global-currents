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
  <link href='https://fonts.googleapis.com/css?family=Arimo:400,700' rel='stylesheet' type='text/css'>

  <!-- CSS
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <link rel="stylesheet" href="../css/normalize.css">
    <link rel="stylesheet" href="../css/skeleton.css">
    <link rel="stylesheet" href="../css/gc.css">
   <!-- <link rel="stylesheet" href="css/lightbox.css">-->

  <!-- JS
    ----------------------------------------- -->
    <script type="text/javascript" src="../javascript/jquery.js"></script>
    <script type="text/javascript" src="../javascript/nav.js"></script>

  <!-- Favicon
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link rel="icon" type="image/png" href="../images/favicon.png">

</head>
<body>

  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
    <div class = "row" id="top-bar"></div>

    <div class="side-bar">
        <?php include 'nav.php' ?>
    </div>

    <div class="page-wrapper">
        <div class="row">
            <div class="ten columns content">
                <?php //include 'search.php' ?>
            </div>
        </div>
    </div>


    <?php
    // Disconnect from database
    $db->close();
    ?>

  <!--<div class="preview" align="center" style="display: none;">
      <img name="preview"' src="images/img1.jpg" alt=""/>
  </div>

  <script src="/javascript/lightbox-plus-jquery.js"></script>-->
<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
</body>
</html>

<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
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


<!-- Primary Page Layout
–––––––––––––––––––––––––––––––––––––––––––––––––– -->
<div id="top-bar"></div>
	<div class="side-bar">
		<ul class="nav">
			<form action="index.php" method="get">
				<fieldset id="feature-search-wrapper">
					<script>document.write(getModule(0));</script>
				</fieldset>

				<input type="button" value="Add a feature" class="add" id="add" />
				<input class="button-primary" type="submit" name="submit" value="Search">
			</form>
		</ul>
	</div>
	<div class="page-wrapper">
			<div class="row">
				<div class="ten columns content">
					<?php include "search.php" ?>
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

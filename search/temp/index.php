<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<title>Search -- Temp</title>
		<link rel="stylesheet" href="main.css">
    	<script type="text/javascript" src="jquery.min.js"></script>
        <script type="text/javascript" src="main.js"></script>
	</head>
	<body>
		<h1>SQL Search</h1>

		<?php include_once "search.php" ?>
		<form action="index.php" method="get">
			<input id="query" name="query" type="text" value="<?php echo getQuery()?>">
			<input type="submit" value="Submit">
			Per page: <select id="perpage" name="perpage">
				<option value="20" selected>20</option>
				<option value="50">50</option>
				<option value="100">100</option>
				<option value="150">150</option>
                <option value="-1">All</option>
			</select>
			Include Errors:<input type="checkbox" name="error" value="true" checked>
			<input type="hidden" name="page" value="0"/>

			<script type="text/javascript">
				document.getElementById('perpage').value = "<?php echo $_REQUEST['perpage'];?>";
				document.getElementByID('error').value = "<?php echo $_REQUEST['error']; ?>"
			</script>
		</form>
        <p><a href="idioms.html" target="_blank">Helpful idioms</a></p>
		<p>Results: <?php echo getNRows(); ?></p>

		<div id="images">
			<?php
			$result = runQuery();
			echo printResults($result);
			?>
		</div>
		<div id="pagination">
			<?php
			echo printPagination();
			?>
		</div>



		<?php
		// Disconnect from database
		$db->close();
		?>
	</body>
</html>

<?php

  // Include StanfordDatabase
  //include_once("stanford.database.php");
  include_once("../mysqlConfig.php");
/*
  // Initialize StanfordDatabase
  $db = new StanfordDatabase();

  // Set the connection information
  $db->set_database("g_spatialhistory_globalcurrents");
  $db->set_username("gspatialhistor");
  $db->set_password("globalcurrents2015");
  $db->use_encryption(false);

  try {
      // Connect to the database
      $db->connect();
  }
  catch(Exception $e) {
      // Handle the error gracefully -- usually, you want to display a friendly error message and alert the admin of the problem
      // $e->getMessage() contains the error message associated with the exception thrown by StanfordDatabase

      echo $e->getMessage();
      exit(0);
  }
*/

// Check if connected to database
if ($db->is_connected()) {
  //Check if form is submitted
  if(isset($_GET['submit'])) {

      $ms = $_GET["manuscript"];
      $folio = $_GET["folio-num"];
      if($_GET["folio-num"] != "")
         $folio .= $_GET["folio-rvp"];
      $ln = false;
        if ($_GET["ln"] == "T") $ln = true;
      $ec = false;
        if ($_GET["ec"] == "T") $ec = true;
      $rubric = false;
        if ($_GET["rubric"] == "T") $rubric = true;
      $primaryColors = $_GET["p-color"];
      $primaryStrict = false; // false if match any color
      $secondaryColors = $_GET["s-color"];
      $secondaryStrict = false; // false if match any color
        if ($_GET["s-color-restrict"] == "all") $secondaryStrict = true;


      $features = array();
      if ($ln) $features[] = "Littera_Notabilior";
      if ($ec) $features[] = "Enlarged_Capital";
      if ($rubric) $features[] = "Rubric";

      $whereCond = array();
      //$whereParams = array();
      if ($ms != '') {
          $whereCond[] = "MS_Number = '$ms'";
          //$whereParams[] = $ms;
      }
      if ($folio != ''){
          $whereCond[] = "F_Number = '$folio'";
          //$whereParams[] = $folio;
      }
      if (count($primaryColors) != 0){
          $colorQuery = "(";
          for($i=0; $i < count($primaryColors)-1; $i++){
              $colorQuery .= "Primary_Color = '$primaryColors[$i]' OR ";
              //$whereParams[] = $primaryColors[$i];
          } $colorQuery .= "Primary_Color = '".$primaryColors[count($primaryColors)-1]."')";
            //$whereParams[] = $primaryColors[count($primaryColors)-1];
          $whereCond[] = $colorQuery;
      }

      if (count($features) > 0) {
          $query = "";
          for ($i = 0; $i < count($features) - 1; $i++) {
              $query .= "(SELECT DISTINCT * FROM " . $features[$i];
              if (count($whereCond)) $query .= " WHERE " . implode(" AND ", $whereCond);
              $query .= ") UNION ";
          }
          $query .= "(SELECT DISTINCT * FROM " . $features[count($features) - 1];
          if (count($whereCond)) $query .= " WHERE " . implode(" AND ", $whereCond);
          $query .= ")";

          // Perform test query
          $result = $db->query($query);

          // Print the result
          $itemNumber = 0;
          while ($row = $result->fetch_assoc()) {//foreach ($stmt->fetchAll(PDO::FETCH_ASSOC) as $row){
              $featureURL = $row['URL'];
              $ms = $row["MS_Number"];
              $folio = $row["F_Number"];
              $x = $row['X'];
              $y = $row['Y'];
              $w = $row['W'];
              $h = $row['H'];
              echo "<img src='" . $row['URL'] . "' class = 'thumbnail' alt='MS $ms $folio: $x, $y, $w, $h'/>'";
              /*
              $featureURL = $row['URL'];
              $ms = $row["MS_Number"];
              $folio = $row["F_Number"];

              $fquery = "SELECT * FROM Folio WHERE MS_Number = '$ms' AND Number = '$folio'";
              $fresult = $db->query($fquery);
              $folioRow = $fresult->fetch_assoc();
              $folioURL = $folioRow["URL"];

              //$folioURL = getFolioURL($row);
              $x = $row['X'];
              $y = $row['Y'];
              $w = $row['W'];
              $h = $row['H'];
              echo "<a href='$folioURL' data-lightbox='lb-$itemNumber' data-title='$folioURL: $x,$y,$w,$h'>".
                        "<img onmouseover='preview.src=$itemNumber.src' name='$itemNumber' src='$featureURL' alt=' '/>".
                  "</a>";
              */
          }
      } else echo "Please select at least one feature";
  }
  else {
      echo "Please enter a search";
  }
}

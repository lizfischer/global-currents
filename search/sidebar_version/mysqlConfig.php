<?php
$username = "gspatialhistor";
$password = "globalcurrents2015";
$database = "g_spatialhistory_globalcurrents";
$host = "g-spatialhistory-globalcurrents.sudb.stanford.edu";
$db = new mysqli($host,$username,$password,$database);
if ($db->connect_error) {
    die("Connection failed: " . $db->connect_error);
}

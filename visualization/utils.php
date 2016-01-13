<?php

function getJSON($myquery)
{
    require_once("../mysqlConfig.php");
// Execute query
    $result = $db->query($myquery);
// Stop and print error if the query did not execute successfully
    if (!$result) {
        die('There was an error running the query [' . $db->error . ']');
    }

// Put for every row in the result, JSON encode and put in an array
    $data = array();
    while ($row = $result->fetch_assoc()) {
        $data[] = json_encode($row);
    }

// Close DB Connection
    mysqli_close($db);

// JSON encode the whole array
    return json_encode($data);

}
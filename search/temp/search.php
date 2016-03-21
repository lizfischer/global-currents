<?php

// Include StanfordDatabase
//include_once("stanford.database.php");
include_once("../mysqlConfig.php");

$perpage = 50;
$startat=$_REQUEST['page'] * $perpage;
$lynx = $html = "";

$pages = 0;

function getPerPage(){
    global $perpage, $startat;

    $perpage = $_REQUEST["perpage"];
    $startat = $_REQUEST['page']* $perpage;
}

function getQuery(){
    getPerPage();
    $query = $_REQUEST["query"];
    return $query;

}

function getPages($query){
    $result = $GLOBALS['db']->query($query);
    return ceil($result->rowCount() / $GLOBALS['perpage']);
}

function runQuery(){
    try {
        $query = getQuery();
        if ($_REQUEST["error"]!="true"){
            $query.=" AND IsError=0";
        }
        $result = $GLOBALS['db']->query($query." LIMIT ".$GLOBALS['startat'].",".$GLOBALS['perpage']);
        return $result;
    }

    catch (PDOException $e) {
        print "Error!: " . $e->getMessage() . "<br/>";
        die();
    }
}

function printResults($result){
    $raw_data = $result->fetchAll(PDO::FETCH_ASSOC); //get associative array of query results

    foreach ($raw_data as $row){ // for every row
        $result_wrap = "<div class='result-wrap'>";
        $img = "";
        $data = "<div class='result-data'>";
        foreach (array_keys($row) as $key){ // for every column
            $value = $row[$key];
            if ($key == 'URL'){ // make image tag out of URL
                $img.="<img src='$value'>";
            } elseif ($key != 'Notes'){ // put rest of data (except notes) in a hidden div
                $data.="<span class='data-item'>$key: $value</span>";
            }
        }
        echo $result_wrap.$img.$data."</div>"."</div>";
    }
}

function printPagination(){
    global $perpage;
    $query = getQuery();
    $error = $_REQUEST['error'];
    $pages = getPages($query);
    for ($k=0; $k<$pages; $k++) {
        if ($k != $_REQUEST['page']) {
            echo " <a href=\"index.php"."?query=$query&page=$k&perpage=$perpage&error=$error\">".($k+1)."</a>";
        } else {
            echo " <b>-".($k+1)."-</b>";
        }
    }
}



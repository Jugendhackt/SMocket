<?php

$id = $_GET["id"];
$new_name = $_GET["newName"];

include "db.php";

$sql_befehl = "UPDATE sockets SET name='" . $new_name . "' WHERE id='" . $id ."';";
if ($conn->query($sql_befehl)) {
  echo "true";
} else {
  echo "false";
}

close($conn);
?>

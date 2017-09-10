<?php
 include "db.php";

 $id = $_GET["id"];
 $new_value = $_GET["value"];

//Value überprüfen
if (!($new_value == 0 || $new_value == 1)) {
  die("Fatal Error: Der Parameter 'Value' hat einen falschen Wert!");
}


//Python Script auffrufen, um Lampenstatus zu ändern
$cmd = "/usr/bin/python3 /home/pi/Smocket/RasPi/gpioswitch.py ". $id . " " . $new_value; 
//echo $cmd;

exec($cmd);

//Datenbank anpassen
$sql_befehl = "UPDATE sockets SET status='". $new_value . "' WHERE id='". $id . "';";
$conn->query($sql_befehl);

?>

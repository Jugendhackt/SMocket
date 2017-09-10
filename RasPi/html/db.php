<?php
header("Access-Control-Allow-Origin: *");

//Config
$server = "localhost";
$username = "phpscript";
$password = "cologne17";

function connect() {
  global $server, $username, $password;

  //Erstelle Verbindungs-Objekt
  $conn = mysqli_connect($server, $username, $password, "smocket");

  //Überprüfen, ob alles funktioniert hat
  if (!$conn) {
      die("Connection failed: " . mysqli_connect_error());
  }
  //echo "Connected successfully";
  return $conn;
}

//Verbinung global machen
$conn = connect();

//Verbindung schließen
function close($conn) {
    mysqli_close($conn);
    //echo "Closed";
}

?>

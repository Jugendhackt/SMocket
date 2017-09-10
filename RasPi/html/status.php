<?php
//Header anpassens
include "db.php";

//Abfrage erstellen
$sql_befehl = "SELECT id, name, status FROM sockets";
$result = $conn->query($sql_befehl);

$count = 0;

//Nur um auf Nummer sicher zu gehen
if ($result->num_rows > 0) {
  //Erstelle für jede "row" einen Datensatz und speichere
  //diesem im Array
  while($row = $result->fetch_assoc()) {
    //Rückgabearray leer machen
    $final = array();
    $count++;

    array_push($final,array(
      "id"=>$row["id"],
      "name"=>$row["name"],
      "status"=>$row["status"]
    ));

    //Trenner für die App hinzufügen
    if ($count != 1) {
         echo "|";
    }

    //Array ausgeben
    echo json_encode( $final);
  }
}

close($conn);
?>

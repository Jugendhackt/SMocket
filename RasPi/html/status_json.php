<?php
//Header anpassens
include "db.php";

//Abfrage erstellen
$sql_befehl = "SELECT id, name, status FROM sockets";
$result = $conn->query($sql_befehl);

$count = 0;

//Nur um auf Nummer sicher zu gehen
if ($result->num_rows > 0) {
    //Datensatz ausgeben
    echo json_encode($result->fetch_all(MYSQLI_ASSOC));
}

close($conn);
?>

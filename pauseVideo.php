<?php
    $db = new mysqli('MYSQL_HOST','MYSQL_USER','MYSQL_PASS','MYSQL_DB');

    $query = "INSERT INTO  `sql5122664`.`commands` (`command`, `video`) VALUES ('pause', 'none')";
    $run = mysqli_query($db, $query);

    if($run) {
        echo "Command was added Successfully";
    } else {
        echo "The command could not be added.";
    }
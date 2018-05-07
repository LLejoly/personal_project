<?php
   $serverName ="localhost";
   $username ="root";
   $password ="";
   $database = "freezer";
   $connectDB = mysqli_connect($serverName, $username, $password, $database);
   $_SERVER['key_encrypt'] = '93';

   if (mysqli_connect_errno()) {
      printf("connection error: %s\n", mysqli_connect_error());
      exit();
   }
?>

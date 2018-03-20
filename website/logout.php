<?php
   session_start();
   if (session_destroy()) {
      mysqli_close($connectDB);
      header("Location: login.php");
   }

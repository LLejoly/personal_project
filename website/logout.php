<?php
// This script allows to log out an active session an redirect it on the 
// user login page
session_start();
if (session_destroy()) {
  mysqli_close($connectDB);
  header("Location: login.php");
}
?> 
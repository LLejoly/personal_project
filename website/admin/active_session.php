<?php
// check if the admin session is still alive or not.
// If it is not the case. The admin user will be redirected to the login page.
include('../connectDB.php');
session_start();

// the admin is not active anymore
if (!isset($_SESSION['login_user'])) {
  header("location: login.php");
}
?> 
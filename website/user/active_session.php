<?php
include('../connectDB.php');
session_start();

$result = mysqli_query($connectDB, "SELECT email FROM User WHERE email = '" . $_SESSION['login_user'] . "'");
$row    = mysqli_fetch_array($result, MYSQLI_ASSOC);

# the user is not active anymore
if (!isset($_SESSION['login_user']) || empty($row)) {
  header("location:../login.php");
}
?> 
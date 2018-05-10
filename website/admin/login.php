<!DOCTYPE html>
<?php
// This page is used to have access to the admin panel.

// define the identifier and the password of the 
// admin. For a practical use this password should be store
// into the htaccess file of the server of into another secure file
// that cannot be accesed by malicious people.
$adminId   = "admin";
$adminPass = "root";

include('../connectDB.php');
session_start();
#the session is active
if (isset($_SESSION['login_user'])) {
  header("location: admin_interface.php");
}

$error = "";

// Obtain data sent with the form
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $userId       = mysqli_real_escape_string($connectDB, $_POST['identifier']);
  $userPassword = mysqli_real_escape_string($connectDB, $_POST['password']);
  
  if ($userId == $adminId && $userPassword == $adminPass) {
    $_SESSION['login_user'] = $adminId;
    header("location: admin_interface.php");
  } else {
    $error = "Your email or password is invalid";
  }
}
?> 

<html>

<head>
    <!--For Mobile devices-->
    <meta name="viewport" content="initial-scale = 1.0, maximum-scale = 1.0, width = device-width">
    <meta http-equiv="Content-Type" content="text/html; charset = utf-8">
    <title>Admin panel connection</title>
</head>

<body>
    <div style="margin:0 auto; text-align:center;">
        <h1>Admin panel</h1>
        <form class="boxcon" action="" method="post">
            <input type="text" name="identifier" placeholder="your Email" required/>
            <input type="password" name="password" placeholder="your Password" required/>
            <input type="submit" value="Connection" />
            <br />
        </form>
        <div class="error">
            <?php echo $error;?>
        </div>
    </div>
</body>

</html>
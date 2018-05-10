<!DOCTYPE html>
<?php
// This page is used to create a new account on the freezer database.
Include('connectDB.php');
$error = "";

if (isset($_POST['submit'])) {
  $error = "";
  if (!strcmp($_POST['email'], '') || strcmp($_POST['password'], $_POST['repassword'])) {
    echo $error = "Not the same password!!";
  } else {
    $email    = mysqli_real_escape_string($connectDB, $_POST['email']);
    $password = mysqli_real_escape_string($connectDB, $_POST['password']);
    $password = crypt($password, $_SERVER['key_encrypt']); #encrypt the password with a salt
    $lang     = mysqli_real_escape_string($connectDB, $_POST['language']);
    $token    = bin2hex(random_bytes(32)); #secure random 1 byte = 2 hexadecimal
    $learning = "[0,0]";
    $sql      = "INSERT INTO User(token, password, email, language, learning) VALUES('$token', '$password', '$email', '$lang', '$learning')";
    $res      = mysqli_query($connectDB, $sql);
    
    if ($res) {
      header("location: login.php");
    } else {
      $error = "An account with this email already exists!";
    }
  }
}
?> 

<html>

<head>
    <!--For Mobile devices-->
    <meta name="viewport" content="initial-scale = 1.0, maximum-scale = 1.0, width = device-width">
    <meta http-equiv="Content-Type" content="text/html; charset = utf-8">
    <link rel="stylesheet" href="./css/login.css">
    <title> Sign up </title>
</head>

<div class="connectPanel">
    <h1> Sign up </h1>
    <form class="boxcon" name="registration" method="post" action="register.php">
        <input type="text" name="email" placeholder="Email" required/>
        <input type="password" name="password" placeholder="Password" required/>
        <input type="password" name="repassword" placeholder="Pass again" required/>
        <input type="submit" name="submit" value="submit">
        <select name="language" required>
            <option value="en">english</option>
            <option value="fr">french</option>
        </select>
    </form>
    <div class="error">
        <?php echo $error;?>
    </div>
    </body>

</html>
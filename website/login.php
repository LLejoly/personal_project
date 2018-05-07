<!DOCTYPE html>
<?php
   include('connectDB.php');
   session_start();
   #the session is active
   if(isset($_SESSION['login_user'])) {
      header("location: ./user/user_interface.php");
   }

   $error = "";

   if ($_SERVER["REQUEST_METHOD"] == "POST") {
      $email = mysqli_real_escape_string($connectDB, $_POST['email']);
      $mypassword = mysqli_real_escape_string($connectDB, $_POST['password']);
      $mypassword = crypt($mypassword, $_SERVER['key_encrypt']); # encrypt the password with a salt DES and compare the encryption with the database
      #test password loiclejoly@gmail.com lolo7890

      $query = "SELECT token FROM User where email = '$email' and password = '$mypassword'";
      $result = mysqli_query($connectDB, $query);
      $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
      $count = mysqli_num_rows($result);

      if ($count == 1) {
         $_SESSION['login_user'] = $email;
         $_SESSION['token'] = $row["token"];
         header("location: ./user/user_interface.php");
      }else {
         $error = "Your email or password is invalid";
      }
   }
?>

<html>
   <head>
      <meta name = "viewport" content = "initial-scale = 1.0, maximum-scale = 1.0, width = device-width"> <!--For Mobile devices-->
      <meta http-equiv = "Content-Type" content = "text/html; charset = utf-8">
      <link rel = "stylesheet" href = "./css/login.css">

      <title> Sign in </title>
   </head>

   <body>
      <div class ="connectPanel">
         <h1> Sign in </h1>
         <form class= "boxcon" action = "" method = "post">
            <input type = "text" name = "email" placeholder="your Email" required/>
            <input type = "password" name = "password" placeholder="your Password" required/>
            <input type = "submit" value = "Connection"/><br />
         </form>

         <a class="register" href="./register.php"> Sign up </a>
         <div class="error"><?php echo $error;?></div>
      </div>
   </body>
</html>

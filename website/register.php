<!DOCTYPE html>
<?php
   Include('connectDB.php');
   $error = "";

   if (isset($_POST['submit'])) {
    $error = "";
    if (!strcmp($_POST['email'],'') || strcmp($_POST['password'], $_POST['repassword'])) {
         echo $error = "Pas le même mot de passe !!";
      } else {
         $email = mysqli_real_escape_string($connectDB, $_POST['email']);
         $password = mysqli_real_escape_string($connectDB,$_POST['password']);
         $lang = mysqli_real_escape_string($connectDB,$_POST['language']);
         $token = bin2hex(random_bytes(32)); #secure random
         $sql= "INSERT INTO User(email, password,token,language) VALUES('$email', '$password','$token','$lang')";
         $res= mysqli_query($connectDB, $sql);

         if ($res) {
            header("location: login.php");
         } else {
            echo $error = "An account with this email already exists!";
         }
      }
   }
?>

<html>
   <head>
      <link rel = "stylesheet" href = "./css/login.css">
      <title> Register </title>
   </head>

   <div class = "connectPanel">
      <h1> Register </h1>
      <form  class = "boxcon" name = "registration" method = "post" action = "register.php">
         <input type = "text" name = "email" placeholder = "Email" required/>
         <input type = "password" name = "password" placeholder = "Password" required/>
         <input type = "password" name = "repassword" placeholder = "Pass again" required/>
         <input type = "submit" name = "submit" value = "submit">
	<select name="language" required>
	  <option value="en">english</option>
	  <option value="fr">french</option>
	</select>
      </form>
      <div class = "error"><?php echo $error;?></div>
   </body>
</html>


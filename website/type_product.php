<!DOCTYPE html>
<?php
   include('connectDB.php');
   session_start();
   $error = "";

   if ($_SERVER["REQUEST_METHOD"] == "POST") {
      $type_name_fr = mysqli_real_escape_string($connectDB, $_POST['french_name']);
      $type_name_en = mysqli_real_escape_string($connectDB, $_POST['english_name']);
      $sql_insert = "INSERT INTO Description_type(type_name_en, type_name_fr) VALUES('$type_name_en', '$type_name_fr')";
      $res = mysqli_query($connectDB, $sql_insert);
      // $mypassword = crypt($mypassword, $_SERVER['key_encrypt']); # encrypt the password with a salt to compare with the one in the database
      //
      // $query = "SELECT token FROM User where email = '$email' and password = '$mypassword'";
      // $result = mysqli_query($connectDB, $query);
      // $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
      // $count = mysqli_num_rows($result);
      //
      // if ($count == 1) {
      //    $_SESSION['login_user'] = $email;
      //    $_SESSION['token'] = $row["token"];
      //    echo "<p> coucou ". $_SESSION['token'] ."</p>";
      //    #header("location: adminPanel.php");
      // }else {
      //    $error = "Your email or password is invalid";
      // }
   }
?>

<!DOCTYPE html>
<?php
  include('active_session.php');
  $message = "";

  if (isset($_POST['submit']))	{
    $name = $_SESSION['login_user'];
    $mypassword = mysqli_real_escape_string($connectDB, $_POST['password']);
    $mypassword = crypt($mypassword, $_SERVER['key_encrypt']); # encrypt the password with a salt to compare with the one in the database
    #test password loiclejoly@gmail.com lolo7890

    $query = "SELECT token FROM User where email = '$name' and password = '$mypassword'";
    $result = mysqli_query($connectDB, $query);
    $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
    $count = mysqli_num_rows($result);
    $newpass = $_POST['newpass'];
    $newpasscheck = $_POST['newpasscheck'];

    if ($count == 1 && strcmp($newpass, $newpasscheck) == 0) {
     $newpassword = mysqli_real_escape_string($connectDB, $newpass);
     $newpassword = crypt($newpassword, $_SERVER['key_encrypt']); # encrypt the password with a salt to compare with the one in the database
     $query = "UPDATE User SET password='$newpassword' where email='$name'";
     $result = mysqli_query($connectDB, $query);
     $message = "<p>Password successfully changed</p>";
    } else {
       $message = "<p>mishmatch with the password</p>";
    }
}
?>

<html>
    <head>
     <meta http-equiv = "Content-Type" content = "text/html; charset = utf-8">
     <link rel = "stylesheet" href = "./css/change_password.css">
   <title>Password Change</title>
    </head>
   <body>
   <h1>Change Password</h1>
  <form class="form-container" method="POST" action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>">
   <h1>Change Password</h1>
    <div id="pass-form">
      <input type="password" name="password" placeholder="current password">
      <input type="password" name="newpass" placeholder="new password">
      <input type="password" name="newpasscheck" placeholder="new password again">
      <?php echo $message; ?>
      <input type="submit" name="submit" value="Update Password">
    </div>
   </form>

   <div style="text-align:center">
  <a class="btn" href="user_interface.php">Home</a>
  <a class="btn" href="../logout.php">Logout</a>
  <div>
  </body>
   </html>

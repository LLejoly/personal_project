<!DOCTYPE html>
<?php
include('active_session.php');
$messagePassword = "";
$messageLanguage = "";
if (isset($_POST['submit'])) {
  switch ($_POST['submit']) {
    case 'password':
      if (isset($_POST['submit'])) {
        $name       = $_SESSION['login_user'];
        $mypassword = mysqli_real_escape_string($connectDB, $_POST['password']);
        $mypassword = crypt($mypassword, $_SERVER['key_encrypt']); # encrypt the password with a salt to compare with the one in the database
        #test password loiclejoly@gmail.com lolo7890
        
        $query        = "SELECT token FROM User where email = '$name' and password = '$mypassword'";
        $result       = mysqli_query($connectDB, $query);
        $row          = mysqli_fetch_array($result, MYSQLI_ASSOC);
        $count        = mysqli_num_rows($result);
        $newpass      = $_POST['newpass'];
        $newpasscheck = $_POST['newpasscheck'];
        
        if ($count == 1 && strcmp($newpass, $newpasscheck) == 0) {
          $newpassword     = mysqli_real_escape_string($connectDB, $newpass);
          $newpassword     = crypt($newpassword, $_SERVER['key_encrypt']); # encrypt the password with a salt to compare with the one in the database
          $query           = "UPDATE User SET password='$newpassword' where email='$name'";
          $result          = mysqli_query($connectDB, $query);
          $messagePassword = "<p>Password successfully changed</p>";
        } else {
          $messagePassword = "<p>miss match with the password</p>";
        }
      }
      break;
    case 'language':
      if (isset($_POST['submit'])) {
        $newlang         = mysqli_real_escape_string($connectDB, $_POST['langlist']);
        $token           = $_SESSION['token'];
        $query           = "UPDATE User SET language='$newlang' where token='$token'";
        $result          = mysqli_query($connectDB, $query);
        $messageLanguage = "<p>language successfully changed</p>";
        break;
      }
  }
}
?>
<html>

<head>
  <!--For Mobile devices-->
  <meta name="viewport" content="initial-scale=1.0, maximum-scale = 1.0, width = device-width">
  <meta http-equiv="Content-Type" content="text/html; charset = utf-8">
    <!--Link for style of table -->
  <link rel="stylesheet" href="../bootstrap/css/bootstrap.css">
  <link rel="stylesheet" href="./css/panel.css">
  <link rel="stylesheet" href="./css/change_password.css">
  <link rel="stylesheet" href="./css/footer.css">

  <title>User Panel</title>
</head>

<body>
  <a href="../logout.php" class="btn btn-secondary btn-lg" style="float:right; margin:16px" role="button">
    <span class="glyphicon glyphicon-log-out"></span> Log out
  </a>

  <header>
    <h1> Welcome
      <?php echo "<i>" . $_SESSION['login_user']. "</i>";?> to the user panel </h1>
  </header>

  <section>
    <h2> User panel </h2>
    <p>
      Welcome on the user panel. This panel is used to give you some information about your account. This interface is very simple
      at the moment and gives your just the minimum information that you need to use the freezer API with third part applications.
    </p>
    <h2> Account information </h2>
    <p>Login:
      <?php echo $_SESSION['login_user']; ?>
    </p>
    <p>Token:
      <?php echo $_SESSION['token']; ?>
    </p>

    <?php 
      $token = $_SESSION['token'];
      $query = "SELECT language FROM User where token = '$token'";
      $result = mysqli_query($connectDB, $query);
      $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
      echo '<p> Language: ' . $row['language'] . '</p>';
    ?>
    <form class="form-container" method="POST" action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>">
      <h1>Change language</h1>
      <div id="pass-form">
        <select name="langlist">
          <option value="en">English</option>
          <option value="fr">Francais</option>
        </select>
        <?php echo $messageLanguage; ?>
        <input type="submit" name="submit" value="language">
      </div>
    </form>

    <form class="form-container" method="POST" action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>">
      <h1>Change Password</h1>
      <div id="pass-form">
        <input type="password" name="password" placeholder="current password">
        <input type="password" name="newpass" placeholder="new password">
        <input type="password" name="newpasscheck" placeholder="new password again">
        <?php echo $messagePassword; ?>
        <input type="submit" name="submit" value="password">
      </div>
    </form>

  </section>

  <footer class="footer-basic-centered">
    <p> Website built by: Loïc Lejoly </p>
    <p> University of Liège </p>
  </footer>
</body>

</html>
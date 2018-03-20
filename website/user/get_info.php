<?php
   include('active_session.php');
?>
<html>
   <head>
      <meta name = "viewport" content = "initial-scale=1.0, maximum-scale = 1.0, width = device-width"> <!--For Mobile devices-->
      <meta http-equiv = "Content-Type" content = "text/html; charset = utf-8">
      <link rel = "stylesheet" href = "./css/panel.css">
      <link rel = "stylesheet" href = "./css/tablecss.css"> <!--Link for style of table -->

      <title>Admin Panel</title>
   </head>
   <body>
      <p>Login: <?php echo $_SESSION['login_user']; ?></p>
      <p>Token: <?php echo $_SESSION['token']; ?></p>
   </body>
   </html>

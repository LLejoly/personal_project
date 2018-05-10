<!DOCTYPE html>
<?php
// This file is used to display the admin panel

include('active_session.php');
$message = "";
if (isset($_POST['submit'])) {
  switch ($_POST['submit']) {
    case 'addType':
      if (isset($_POST['submit'])) {
        $type_name_fr = mysqli_real_escape_string($connectDB, $_POST['french_name']);
        $type_name_en = mysqli_real_escape_string($connectDB, $_POST['english_name']);
        $sql_insert   = "INSERT INTO Description_type(type_name_en, type_name_fr) VALUES('$type_name_en', '$type_name_fr')";
        $res          = mysqli_query($connectDB, $sql_insert);
        // Refresh the page after the element added
        header("Refresh:0");
      }
  }
}

// This function is used to display the different
// types of products present in the database 
function displayTypes() {
  global $connectDB;
  $error = "";
  $table = '<table class="tableLib"><tr><th>ID</th><th>type_name_en</th><th>type_name_fr</th></tr>';
  
  $query  = "SELECT * FROM Description_type";
  $result = mysqli_query($connectDB, $query);
  $rows   = mysqli_fetch_all($result, MYSQLI_ASSOC);
  //Display each product type
  foreach ($rows as $row) {
    $table .= "<tr>";
    $table .= "<td>" . $row['type_id'] . "</td>";
    $table .= "<td>" . $row['type_name_en'] . "</td>";
    $table .= "<td>" . $row['type_name_fr'] . "</td>";
    $table .= "</tr>";
  }
  
  $table .= "</table>";
  echo $table;
}
?>

<html>

<head>
  <meta name="viewport" content="initial-scale=1.0, maximum-scale = 1.0, width = device-width">
  <!--For Mobile devices-->
  <meta http-equiv="Content-Type" content="text/html; charset = utf-8">
  <link rel="stylesheet" href="../bootstrap/css/bootstrap.css">
  <link rel="stylesheet" href="./css/formstyle.css">
  <link rel="stylesheet" href="./css/tablecss.css">
  <link rel="stylesheet" href="./css/footer.css">
  <!--Link for style of table -->

  <title>Admin Panel</title>
</head>

<body>
  <a href="../logout.php" class="btn btn-secondary btn-lg" style="float:right; margin:16px" role="button">
    <span class="glyphicon glyphicon-log-out"></span> Log out
  </a>

  <header>
    <h1> Welcome
      <?php echo "<i>" . $_SESSION['login_user'] . "</i>";?> to the admin panel</h1>
  </header>

  <section>
    <h2>Admin panel</h2>
    <p>
      Welcome on the admin panel. The panel  is really simple it only gives the different types of products and the possibility
      to add a new type of product.
    </p>
    <h2>Display types</h2>
    <p> To display/hide the types please click on the button:</p>
    <button id="typeBtn" onclick="setVisibility('types_section')">Click me</button>
    <div id="types_section" style="display:none">
      <?php displayTypes(); ?>
    </div>

    <h2>Add a new type of product</h2>

    <form class="form-container" method="POST" action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>">
      <h1>Add a new type</h1>
      <div id="pass-form">
        <input type="text" name="french_name" placeholder="french name">
        <input type="text" name="english_name" placeholder="english name">
        <?php echo $message; ?>
        <input type="submit" name="submit" value="addType">
      </div>
    </form>
  </section>

  <footer class="footer-basic-centered">
    <p> Website built by: Loïc Lejoly </p>
    <p> University of Liège </p>
  </footer>
</body>
<script>
  // This function allows to set the visibility of an element
  // If the element is already visible then it will be turned to none
  // otherwise an element which is set to none will be turned to block.
  // elementId: It is the id given to a element
  function setVisibility(elementId) {
    if (document.getElementById(elementId).style.display == 'none') {
      document.getElementById(elementId).style.display = 'block';
      document.getElementById('typeBtn').innerHTML = 'Hide';
    } else {
      document.getElementById(elementId).style.display = 'none';
      document.getElementById('typeBtn').innerHTML = 'Show';
    }
  }
</script>

</html>
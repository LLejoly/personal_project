<?php
   include('connectDB.php');
   session_start();
   $error = "";
   $table = '<table class=".tableLib" style="width:100%"><tr><th>ID</th><th>type_name_en</th><th>type_name_fr</th></tr>';

   if ($_SERVER["REQUEST_METHOD"] == "GET") {
      $query = "SELECT * FROM Description_type";
      $result = mysqli_query($connectDB, $query);
      $rows = mysqli_fetch_all($result, MYSQLI_ASSOC);
      foreach ($rows as $row) {
        $table .= "<tr>";
        $table .= "<td>". $row['type_id']."</td>";
        $table .= "<td>". $row['type_name_en']."</td>";
        $table .= "<td>". $row['type_name_fr']."</td>";
        $table .= "</tr>";
      }

      $table .= "</table>";
      echo $table;
   }
?>

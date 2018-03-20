<!DOCTYPE html>
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
      <header>
         <h1> Bienvenu sur l'admin panel </h1>
      </header>

      <nav>
         <ul>
            <li class = "connected"> <?php echo "<p> hello, " . "<i>" . $_SESSION['login_user']. "</i>" . "</p>";?> </li>
            <li><a class = "active" href="change_password.php">Change password</a></li>
            <li><a href = "get_info.php"> Account details</a></li>
            <li><a href = "../logout.php"> Logout </a></li>
         </ul>
      </nav>

      <section>
         <h1> Fonctionnement du panel: </h1>
            <p>
               Bienvenu sur l'admin panel du site. Vous pourrez retrouver sur ce panel différentes informations concernant la base de données
               regroupant les différentes informations de la bibliothèque de jeux vidéos. Dans le menu à gauche vous pouvez retrouver l'ensemble des onglets disponibles.
            </p>

         <h2> Bibliothèque: </h2>
            <p>
               L'onglet bibliothèque permet d'avoir accès au données présentes dans la base mysql il vous suffit juste de sélectionner la table
               que vous désirez afficher et ensuite de sélectionner les différents champs vous intéressant.
            </p>

         <h2> Fonctionnel: </h2>
            <p>
               L'onglet nouvel exemplaire permet d'ajouter un nouvel exemplaire à votre bibliothèque d'exemplaires existant déjà.
               L'onglet fonctionnel permet d'interroger votre base de données pour connaître les jeux qui sont encore en état de fonctionner.
               Un exemplaire physique est jugé fonctionnel lorsque son état est strictement supérieur à 1.
               Un exemplaire virtuel quant à lui est jugé fonctionnel lorsque qu'il est au moins capable de fonctionner sur
               un émulateur lui même capable de fonctionner sur au moins un système.
            </p>

         <h2> Performance </h2>
            <p> L'onglet performance permet d'évaluer la performance d'un émulateur en comptabilisant le nombre d'exemplaires virtuels qu'un
               émulateur peut faire fonctionner divisé par le nombre total d'exemplaires virtuels fonctionnels.
            </p>

         <h2> Recommandation </h2>
            <p>
               L'onglet recommandation permet de donner une liste de recommandations des 5 meilleurs jeux auxquels l'utilisateur
               n'a pas encore joué et qui fonctionnent.
            </p>
      </section>

      <footer>
         <p> Site réalisé par: Francesco Mirisola, Mathias Beguin, Loic Lejoly </p>
         <p> Université de Liège </p>
      </footer>
   </body>
</html>

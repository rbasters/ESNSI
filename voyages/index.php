<?php
// try {} catch {} => On tente d'exécuter les instructions contenues dans try. Si une erreur survient on l'attrape dans catch
try {

    // on instancie la classe PDO. La documentation nous renseigne sur les 3 arguments à passer au constructeur
    // le DSN, l'utilisateur et le mot de passe
   $pdo = new PDO('mysql:host=localhost;dbname=dunsivoyages', 'root', '');

   // on prépare une requête
   $statement = $pdo->prepare("SELECT * FROM villes ORDER BY libelle");
   // on l'exécute
   $statement->execute();

   // on ramène tous les résultats dans la variable $villes
   $villes = $statement->fetchAll(PDO::FETCH_ASSOC);

} catch (PDOException $e) {

   print "Erreur !: " . $e->getMessage() . "<br/>";
   die();
}
?>

<!doctype html>
<html lang="fr">
 <head>
 <!-- Quelques metas incontournables -->
   <meta charset="utf-8">
   
     <!-- Bug Safari 9 -->
   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
   <title>Calcul du meilleur itinéraire</title>
   
     <!-- un favicon trouvé sur internet qui sera également le logo de notre application -->
   <link rel="shortcut icon" href="https://cdn2.iconfinder.com/data/icons/on-point-social-media/141/Maps-512.png">
   
     <!-- Chargement de Bootstrap -->
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
   
     <!-- Leaflet CSS -->
   <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
   
     <!-- Leaflet JS après le CSS -->
   <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
   
     <!-- notre feuille de style -->
   <link rel="stylesheet" href="../css/app.css">
   
     <!-- notre fichier Javascript -->
   <script src="../js/app.js" async defer></script>
 </head>
 <body>
 <!-- bloc de contenu principal -->
 <div class="main-content">

 <!-- la barre de navigation (qui ne servira à rien dans notre application) -->
 <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
   <a class="navbar-brand" href="#">
       <img src="https://cdn2.iconfinder.com/data/icons/on-point-social-media/141/Maps-512.png" width="30" height="30" alt="">
   </a>

   <div class="collapse navbar-collapse" id="navbarSupportedContent">
       <ul class="navbar-nav mr-auto">
           <li class="nav-item active">
               <a class="nav-link" href="#">Accueil <span class="sr-only">(current)</span></a>
           </li>
           <li class="nav-item">
               <a class="nav-link" href="#">Lien 2</a>
           </li>
           <li class="nav-item">
               <a class="nav-link" href="#">Lien 1</a>
           </li>
       </ul>
   </div>
 </nav>
     
 <!-- conteneur principal -->
 <div class="container">
     <!-- titre principal -->
     <h1>Calculez votre itinéraire</h1>

     <!-- message informatif -->
    <div class="information alert alert-secondary" role="alert">
        Pour trouver un itinéraire, cliquez sur 2 marqueurs de la carte ou choisissez 2 villes dans les listes de sélection.
    </div>

     <div class="row">
         <!-- première colonne : accueillera la carte -->
         <div class="col-md-8">
             <!-- la carte de France -->
             <div id="mapid"></div>
         </div>

         <!-- deuxième colonne -->
         <div class="col-md-4">
             <!-- formulaire pour pouvoir poster nos choix de villes -->
            <form method="post">
               <div class="form-group">
                   <label for="villedepart">Aller de :</label>
                    <select class="form-control" id="villedepart" name="villedepart">
                       <?php foreach($villes as $ville) : ?>
                       <option value="<?= $ville['id'] ?>"><?= $ville['libelle'] ?></option>
                       <?php endforeach ?>
                    </select>
                   <small id="villeDHelp" class="form-text text-muted">Choisissez une ville de départ</small>
               </div>

               <div class="form-group">
                   <label for="villearrivee">à :</label>
                    <select class="form-control" id="villearrivee" name="villearrivee">
                       <?php foreach($villes as $ville) : ?>
                       <option value="<?= $ville['id'] ?>"><?= $ville['libelle'] ?></option>
                       <?php endforeach ?>
                    </select>
                   <small id="villeAHelp" class="form-text text-muted">Choisissez une ville d'arrivée</small>
               </div>

               <button type="submit" class="btn btn-primary btn-block">Trouver l'itinéraire le plus court&nbsp; &rarr;</button>
             </form>
             
             <!-- Conteneur pour afficher le résultat -->
             <div class="resultat"></div>
         </div>
     </div>

 </div>
</div>

  <!-- Pied de page -->
  <footer>
   <div class="container">
       <div class="row">
           <div class="col">
               <a href="">@copyright Joachim Lucas 2020</a>
           </div>
       </div>
   </div>
  </footer>

 </body>
</html>
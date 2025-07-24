# Utilisez les bases de Python pour l'analyse de marché

### PROJECT BRIEF

🕒 50 hours
Last updated on Friday, July 9, 2021



Vous êtes analyste marketing chez Books Online, une importante librairie en ligne spécialisée dans les livres d'occasion. Dans le cadre de vos fonctions, vous essayez de suivre manuellement les prix des livres d’occasion sur les sites web de vos concurrents, mais cela représente trop de travail et vous n’arrivez pas à y faire face : il y a trop de livres et trop de librairies en ligne ! Vous et votre équipe avez décidé d’automatiser cette tâche laborieuse via un programme (un scraper) développé en Python, capable d’extraire les informations tarifaires d’autres librairies en ligne.


![logo.png](img/logo.png)
# BOOK TO SCRAP


Sam, votre responsable d’équipe, vous a chargé de développer une version bêta de ce système pour suivre les prix des livres chez Books to Scrape, un revendeur de livres en ligne. En pratique, dans cette version bêta, votre programme n’effectuera pas une véritable surveillance en temps réel des prix sur la durée. Il s’agira simplement d’une application exécutable à la demande visant à récupérer les prix au moment de son exécution.

Sam vous a envoyé l’e-mail suivant :

----------------------------------------------------------------------------------------------------------------------

Objet : Programme d’extraction des prix
À : Vous
De : Sam

Bonjour !
J’espère que vous pourrez m’aider à créer un système de surveillance des prix. Pour élaborer une version bêta du système limitée à un seul revendeur, le mieux est probablement de suivre les étapes que j’ai définies ci-dessous.
Choisissez n’importe quelle page Produit sur le site de Books to Scrape. Écrivez un script Python qui visite cette page et en extrait les informations suivantes :

- product_page_url
- universal_product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

Écrivez les données dans un fichier CSV qui utilise les champs ci-dessus comme en-têtes de colonnes.

Maintenant que vous avez obtenu les informations concernant un premier livre, vous pouvez essayer de récupérer toutes les données nécessaires pour toute une catégorie d’ouvrages. Choisissez n’importe quelle catégorie sur le site de Books to Scrape. Écrivez un script Python qui consulte la page de la catégorie choisie, et extrait l’URL de la page Produit de chaque livre appartenant à cette catégorie. Combinez cela avec le travail que vous avez déjà effectué afin d’extraire les données produit de tous les livres de la catégorie choisie, puis écrivez les données dans un seul fichier CSV.
**Remarque** : certaines pages de catégorie comptent plus de 20 livres, qui sont donc répartis sur différentes pages (« pagination »). Votre application doit être capable de parcourir automatiquement les multiples pages si présentes.
Ensuite, étendez votre travail à l’écriture d’un script qui consulte le site de Books to Scrape, extrait toutes les catégories de livres disponibles, puis extrait les informations de tous les livres appartenant à toutes les différentes catégories, ce serait fantastique ! Vous devez écrire les données dans un fichier CSV distinct pour chaque catégorie de livres.
Enfin, prolongez votre travail existant pour télécharger et enregistrer le fichier image de couverture de chaque livre que vous consultez !
Une fois ce projet réalisé, veillez à enregistrer votre code dans un repository GitHub et à effectuer des commits réguliers accompagnés de messages de commit clairs. N’oubliez pas que vous devez également ajouter un fichier README.md bien structuré expliquant le fonctionnement de votre programme. Je veux m’assurer que je peux lire et analyser vos fichiers CSV. Vous devez donc m’envoyer une version exécutable du programme (via GitHub et un fichier README.md, où vous ajouterez dans le repository afin que je puisse exécuter le code correctement et produire quelques données !
Cordialement,

**Sam**
**Responsable d’équipe**
**Books Online**

----------------------------------------------------------------------------------------------------------------------

Ces besoins étant clarifiés, vous êtes prêt à mettre votre maîtrise de Python toute neuve au service de votre équipe !

#### Livrables :

- Un lien vers un repository GitHub qui doit contenir les éléments suivants :
- l’ensemble de votre code d’application ;
- le fichier requirements.txt, mais pas l’environnement virtuel lui-même ;
- un fichier README.md expliquant comment créer et activer l’environnement virtuel, puis exécuter le code d’application ;
- les données/images extraites ne doivent pas faire partie du repository lui-même.
- Un fichier compressé contenant toutes les données extraites et les images associées dans un format ou une structure facile à suivre.

ℹ️ ***Pour faciliter votre passage au jury, déposez sur la plateforme, dans un dossier nommé
"P2_nom_prénom", tous les livrables du projet. Chaque livrable doit être nommé avec le numéro du projet et selon l’ordre dans lequel il apparaît, par exemple "P2_01_codesource",
"P2_02_codesource", et ainsi de suite.***

#### Soutenance :

Lors de la présentation orale, votre évaluateur jouera le rôle de Sam, votre responsable d’équipe.
Il mettra en doute vos décisions, alors soyez prêt à défendre votre travail. La présentation sera structurée comme suit :

• **Présentation des livrables (15 minutes)**

  * Présentez l’application en décrivant le processus utilisé pour l’écrire et en mettant en évidence les éléments extraction, transformation et chargement du code.
  
  * Faites à votre évaluateur une démonstration de l’application en l’exécutant en "direct".
  
  * Présentez des idées d’améliorations futures du code.
  
• **Discussion (10 minutes)**

  * En jouant le rôle d’un responsable d’équipe, l’évaluateur vous posera des questions sur votre méthode et vos livrables.
 
• **Débriefing (5 min)** 

 * À la fin de la session, l’évaluateur cessera de jouer le rôle du responsable d’équipe afin que vous puissiez effectuer le débriefing ensemble.

#### Compétence transversale

En plus des compétences spécialisées énumérées ci-dessous, concentrez-vous sur le développement et la démonstration de la communication en tant que compétence transversale (ou "soft skill"). Elle sera essentielle pour votre réussite dans ce projet et les suivants, ainsi que dans votre future carrière. N'hésitez pas à demander à votre mentor un retour au cours de la réalisation de votre projet.

#### Compétences cibles : 

- Gérer les données à l'aide du processus ETL
- Utiliser le contrôle de version avec Git et GitHub
- Appliquer les bases de la programmation en Python
- Configurer un environnement Python


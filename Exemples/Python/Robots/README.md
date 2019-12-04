# Un robot simple

Modéliser un robot capable d’avancer d’une case en fonction d'une direction (nord, sud, ouest, est) et de pivoter de 90˚ vers la droite

## Une première version avec des fonctions et un dictionnaire (hashmap) définie dans un module

* Pas de définition explicite du type Robot
    * les données du robot sont stockées dans un dictionnaire (type dict), tableau associatif
    * syntaxe un peu lourde : r[’x’]
les notions d’objet et de classe seront de meilleures solutions
    * Remarque : on pourrait utiliser le type namedtuple de collections (mais immuable).
* Type énuméré Direction représenté par un entier.
    * Remarque : Python offre le module enum pour définir des types énumérés.
* _dx et _dy sont des tuples indicés par la direction du robot
    * donnent l’entier à ajouter à x ou y pour déplacer le robot en fonction de sa direction
    * simplification du code de translater, évite des if.
* _directions permet d’obtenir le nom en clair de la direction
    * utilisé à la création
    * utilisé à l’affichage
* les éléments qui commencent pas un souligné (_) sont considérés comme locaux
    * un utilisateur du module ne devrait pas les utiliser
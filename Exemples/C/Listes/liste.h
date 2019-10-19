/* Pour installer gcc "sudo apt install build-essential" */
#define MAX 100
/**
 * Liste d'entiers
 */
struct _liste {
   int taille;
   int contenu[]; 
};

typedef struct _liste Liste;

/**
 * Les opérations de liste
 * En C pour un type de donnée l'effort est fait par le programmeur
 * Pour regrouper les données et traitement
 */
Liste *creerListe();
void ajouter(Liste *l, int e);
void afficher(Liste *l);
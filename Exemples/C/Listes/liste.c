#include "liste.h"
#include <stdlib.h>
#include <stdio.h>

/** Crátion d'une référence de liste
 */
Liste *creerListe() {
    Liste *l;
    l=malloc(sizeof(struct _liste)*MAX);
    l->taille=0;
    return (Liste *)l;
}

/** Ajouter élement à la liste
 */
void ajouter(Liste *l, int e){
    l->contenu[l->taille]=e;
    l->taille++;
}

/** Afficher la liste [e_0, e_1, ..., e_taille-1]
 */
void afficher(Liste *l){
    int i=0;
    //Afficher le debut de la liste
    printf("[");
    while (i < l->taille-2) {
        printf("%d, ",l->contenu[i]);
        i++;
    }
    //i>=l->taille-2 cad taille-1 qui est le dernier élément
    printf("%d]\n",l->contenu[i]);
}


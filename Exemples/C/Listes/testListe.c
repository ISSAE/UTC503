#include "liste.h"
#include <stdlib.h>
#include <stdio.h>

/** Pour tester le programme
 */
int main(int argc, char **argv) {
    Liste *l = creerListe();
    ajouter(l,1);
    ajouter(l,10);
    ajouter(l,100);
    ajouter(l,10);
    ajouter(l,1);
    afficher(l);
}
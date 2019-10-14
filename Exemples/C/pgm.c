#include <stdio.h>
/* Écrit ene exclamation à l'écran */
int main (int argc, char **argv) {
    int a=0;
    int b=1;
    int x;
    char condition=1;
    printf("Bonjour auditeurs de UTC503");
    if (a==0) {
        x=b;
    } else {
        x=a+b;
    }

    while (a < 2) {
        printf("%d",a);
        if (a==1) {
            x=a-1;
        }
        a=a+1;
    }

    //Un while en C / Java
    while (condition) {
        ...
    }
}
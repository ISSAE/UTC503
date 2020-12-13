#include <stdio.h>

int main(int argc, char **argv) {
    int x = 10;
    int y = 20;
    int z;
    printf("Avant %d %p %d %p\n", x, &x, y, &y);
    //swap
    z=x;
    x=y;
    y=z;
    printf("Après %d %p %d %p\n", x, &x, y, &y);
}
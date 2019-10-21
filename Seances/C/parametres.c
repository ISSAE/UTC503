int f(int x, int y){
    int z=x+y;
    x=2;
    y=3;
    return z;
}

int main(int argc, char**argv) {
    int x;
    int b;

    printf("x dans main=%d, b dans main=%d, f(x,b)=%d",x,b,f(x,b));
}
x = 10
y = 20

print("Avant", x, id(x), y, id(y))

x,y = y,x

print("Avant", x, id(x), y, id(y))


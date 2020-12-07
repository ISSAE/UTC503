x = 10
y = 20

print("Avant", x, id(x), y, id(y))

z = x
x = y
y = z

print("Avant", x, id(x), y, id(y))

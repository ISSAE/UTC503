x = 32
y = 9
op = "+ - * / % // & | and or << >>".split()
for o in op:
    s = str(x) + " " + o + "  " + str(y)
    print(s, " = ", eval(s))

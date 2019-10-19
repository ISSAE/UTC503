n=int(input("Donner un nombre: "))
def diviseur(n):
    res=[1]
    i=2
    while i<n:
        if n%i == 0:
            res.append(i)
        i=i+1
    return res
print(diviseur(n))
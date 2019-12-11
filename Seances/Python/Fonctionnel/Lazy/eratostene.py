def get_premier():
    """lazy Crible d'Eratosthenes

       il s'agit de supprimer d'une table des entiers de 2 à N tous les multiples d'un entier. 
       En supprimant tous les multiples, à la fin il ne restera que les entiers qui ne sont multiples
       d'aucun entier, et qui sont donc les nombres premiers. 
       On commence par rayer les multiples de 2, puis à chaque fois on raye les multiples du plus petit entier restant. 
    """
    candidate = 2
    trouve = []
    while True:
        if all(candidate % prime != 0 for prime in trouve):
            yield candidate
            trouve.append(candidate)
        candidate += 1

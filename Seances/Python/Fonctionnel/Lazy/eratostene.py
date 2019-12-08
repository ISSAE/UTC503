def get_premier():
    "Simple lazy Sieve of Eratosthenes"
    candidate = 2
    trouve = []
    while True:
        if all(candidate % prime != 0 for prime in trouve):
            yield candidate
            trouve.append(candidate)
        candidate += 1

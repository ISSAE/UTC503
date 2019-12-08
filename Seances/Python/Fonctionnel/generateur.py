def get_primes():
     "Simple lazy Sieve of Eratosthenes"
     candidate = 2
     found = []
     while True:
         if all(candidate % prime != 0 for prime in found):
             yield candidate
             found.append(candidate)
         candidate += 1

primes = get_primes()
next(primes), next(primes), next(primes)

for _, prime in zip(range(100), primes):
     print(prime, end=" ")

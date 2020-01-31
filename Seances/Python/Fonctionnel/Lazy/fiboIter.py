class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1
        self.total = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.total += self.a
        return self.a
    def running_sum(self):
        return self.total

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

from itertools import tee, accumulate


if __name__ == '__main__':
    fibo1=Fibonacci()
    fibo2=Fibonacci()
    #Boucle sur des iterables
    for _, i in zip(range(10), fibo1):
       print(i, end=" ")
    #equivalente a celle ci
    for i in range(10):
        print(next(fibo1), end=" ")
    fibo1.running_sum()
    s, t = tee(fibonacci())
    pairs = zip(t, accumulate(s))
    for _, (fib, total) in zip(range(10), pairs):
        print('Pure fonc et itertool', fib, total)
        print('Par objet iterable   ',next(fibo2),fibo2.running_sum())


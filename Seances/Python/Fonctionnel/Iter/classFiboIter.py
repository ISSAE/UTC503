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

# >>> fib = Fibonacci()
# >>> fib.running_sum()
# 0
# >>> for _, i in zip(range(10), fib):
# ...     print(i, end=" ")
# ...
# 1 1 2 3 5 8 13 21 34 55
# >>> fib.running_sum()
# 143
# >>> next(fib)
# 89

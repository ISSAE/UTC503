//Récursif
int fibr(int n)
{
  if (n < 2)
    return n;
  else
    return fib(n - 1) + fib(n - 2);
}

printf("%d\n", fib(10));

//Itératif
int fibi(int n)
{
  int first = 0, second = 1;

  int tmp;
  while (n--)
  {
    tmp = first + second;
    first = second;
    second = tmp;
  }
  return first;
}
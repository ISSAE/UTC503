public class Fibo {
public static void main(String args[]) {
        int N = Integer.parseInt(args[0]);
        System.out.println(fib(N));
    }
public static int fib(int n) {
        if (n < 2)
            return (n);
        return (fib(n - 2) + fib(n - 1));
    }
}
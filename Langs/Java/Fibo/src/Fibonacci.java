import java.util.Scanner;

public class Fibonacci {

    static long fibo(int n) {return (n<2) ? n: fibo(n-2) + fibo(n-1) ;}

    public static void main(String[] args) throws Exception {

    Scanner sc = new Scanner(System.in);

    System.out.println("Type number of numbers: ");
    int len = sc.nextInt();
    
    System.out.println("Fibo Sequence: ");
    for (int i = 0; i < len+1; i++) {
       System.out.printf("%d\n",Fibonacci.fibo(i)); ;
    }
  }

}


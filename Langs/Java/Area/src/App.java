import java.lang.Math.*;
import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        double r,A,pi = Math.PI;;
        
        Scanner read = new Scanner(System.in);
        System.out.println("Type your radius value : ");
        r = read.nextDouble();
        
        A = pi * (r * r);
        System.out.println("With" + r +" of radius\nThe circumference is " + A);
    }
}

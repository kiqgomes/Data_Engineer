import java.util.Scanner;

public class Scan {
    public static void main(String[] args) throws Exception {
        System.out.println("Write your name: ");

        Scanner sc = new Scanner(System.in);
        
        String name = sc.nextLine(); 
        System.out.println("Olá " + name);
    }
}

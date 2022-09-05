package Langs.Java.PipePredictGas.app;

import java.io.File;
import java.util.Scanner;

/**
 * prediction
 */
public class Prediction {

    public static void main(String[] args) {
        
        Scanner sc = null;
        double mileage = 0;
        double theta0 = 0;
        double theta1 = 0;
        int scale = 1000;

        try {
            sc = new Scanner(new File("modelo.txt"));
            String line = sc.nextLine();
            theta0 = Double.parseDouble(line.split(",")[0]);
            theta1 = Double.parseDouble(line.split(",")[1]);
        } catch (Exception e) {
            theta0 = 0;
            theta1 = 0;
        }

        if (sc != null)
            sc.close();
        
        sc = new Scanner(System.in);
        System.out.println("Welcome to my ML model in Java");
        System.out.println("Type the km: ");

        try {
            mileage = Double.parseDouble(sc.nextLine());
        } catch (Exception e) {
            System.out.println("Invalide value");
            System.exit(1);
        }

        System.out.printf("Prevision of gas cost $%d\n",(int)((theta0 + theta1 * mileage/scale)*scale));
    }
    
}
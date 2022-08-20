package com.infnet.mathp;
import java.util.ArrayList;
import java.util.Scanner;

public class DotP {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        
        ArrayList v1 = new ArrayList();
        ArrayList v2 = new ArrayList();
        
        try{
            System.out.println("Put your five numbers to first vec:");
            for (int i = 0; i < 5; i++) {
                v1.add(sc.nextInt());
            }
        }catch (Exception e){
            System.err.println("Just numbers and Integers, Please!");
            System.err.println("Error Message: " + e);
            System.exit(1);
        }
        try {
            System.out.println("Put your five numbers to the second one:");
            for (int i = 0; i < 5; i++) {
                v2.add(sc.nextInt());
            }
        } catch (Exception e) {
            System.err.println("Just numbers and Integers, Please!");
            System.err.println("Error Message: " + e);
            System.exit(1);
        }

        System.out.printf("To confirm Data:\nVector 1 : %s\nVector 2 : %s\n",v1.toString(),v2.toString());

        int dotProd = 0;

        for (int i = 0; i < v1.size(); i++) {
            dotProd += Integer.parseInt(v1.get(i).toString()) * Integer.parseInt(v2.get(i).toString());
        }

        System.out.printf("Your Dot Product is %d\n",dotProd);
    }
}

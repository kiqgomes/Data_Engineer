import java.util.Scanner;
public class TempConvert {
    public static void main(String[] args) throws Exception {
        String r;
        double c,k,f;
        System.out.println("\n-------- Welcome to our temperature converter ---------\n");
        System.out.println("Choice what you want convert\n");
        System.out.println("Type 1 to Celsius in Kelvin");
        System.out.println("Type 2 to Celsius in Fahrenheit\n");

        Scanner read = new Scanner(System.in);
        r = read.next();

        switch (r) {
            case "1":
                System.out.println("Type the Celsius value: ");
                c = read.nextDouble();
                k = c + 273.15;
                System.out.println("\nKelvin temperature: " + k + "K");
                break;
            case "2":
                System.out.println("Type the Celsius value: ");
                c = read.nextFloat();
                f = (c * 1.8) + 32;
                System.out.println("\nFahrenheit temperature: " + f + "°F");
                break;
        
            default:
                System.out.println("We haven't more options by now.\nBut, come back later, how knows hehe");
                break;
        }
    }
}

import java.util.InputMismatchException;
import java.util.Scanner;
public class NumbersDivision {
    public static void main(String[] args) throws Exception {
        double a,b,result;
        Scanner sc = new Scanner(System.in);

        try {

            System.out.println("Type the first number: ");
            a = sc.nextInt();

            System.out.println("Type the second one: ");
            b = sc.nextInt();
            
            result = a/b;
            
            // To handle with Infinity result "problem"
            if (result == Double.POSITIVE_INFINITY){throw new IllegalArgumentException("You can't divide by zero");}
    
            System.out.printf("Here is your result: %.2f",result);

        }catch (InputMismatchException ie) {
            System.err.println("Please use just numbers!!");
            System.err.println("Error: " + ie);
            System.exit(1);  
        }catch (Exception ex){
            System.err.println("Something are wrong!!");
            System.err.println("Error: " + ex);
            System.exit(1);
        }
        finally {
            System.out.println("\nThanks for your time!");
        }
    }
}

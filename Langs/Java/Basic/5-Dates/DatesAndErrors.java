import java.util.Date;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DatesAndErrors {
    
    public static void main(String[] args) {
        
        Date today = new Date();
        System.out.printf("Using the Date package\nToday is %tD\n\n",today);

        LocalDate systemDate = LocalDate.now();
        System.out.printf("Using LocalDate package\nSystem date: %tD\n\n",systemDate);

        LocalDateTime systemDateTime = LocalDateTime.now();
        System.out.printf("Using LocalDateTime package\nSystem date: %tD\n\n",systemDateTime);

        DateTimeFormatter formattedDate = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
        System.out.printf("Using LocalDateTime package with DateTimeFormatter\nSystem formatted date: %s\n\n",systemDateTime.format(formattedDate));

        System.out.println("Calc diference between dates");
        try {
            long start = System.currentTimeMillis(); // Time on milliseconds
            System.out.println(new Date() + "\n");

            //Thread.sleep(5*60*10);
            Thread.sleep(3000);
            
            System.out.println(new Date() + "\n");

            long end = System.currentTimeMillis();
            long diff = end - start;
            System.out.println("Difference -> " + diff);
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }

    }
}

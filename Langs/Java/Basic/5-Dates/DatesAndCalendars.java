import java.util.Date;
import java.util.Calendar;
import java.text.SimpleDateFormat;

public class DatesAndCalendars {
    
    public static void main(String[] args) {
        
        Date today = new Date();
        System.out.println(today.getTime());
        System.out.println(today);

        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        System.out.println(sdf.format(today));

        SimpleDateFormat sdf2 = new SimpleDateFormat("D"); // Year day
        System.out.println(sdf2.format(today));

        Calendar cal = Calendar.getInstance();
        System.out.println(cal);

        cal.setTime(new Date());

        int day = cal.get(Calendar.DATE);
        int month = cal.get(Calendar.MONTH)+1;
        int year = cal.get(Calendar.YEAR);

        System.out.printf("Dia %d do %d de %d\n",day,month,year);

        cal.set(Calendar.DATE, +24);
        System.out.println(cal.toInstant().toString());
    }
}

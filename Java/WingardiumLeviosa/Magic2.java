package WingardiumLeviosa;
import java.util.*;
public class Magic2 {
    public static void main(String[] args) {
        System.out.println("Lambdas");
        // Created a integer array
        ArrayList<Integer> numbers = new ArrayList<>();
        // Added 4 elements
        numbers.add(43);
        numbers.add(58);
        numbers.add(65);
        numbers.add(98);
        // Displayed the elements
        numbers.forEach((x) -> { System.out.println(x); });
        // Finding a specific element
        numbers.forEach(n -> {if (n == 65) {System.out.println("Found " + n);}});
    }
}

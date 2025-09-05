package WingardiumLeviosa;
import java.util.*;
public class Magic2 {
    public static void main(String[] args) {
        System.out.println("Lambdas");
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(43);
        numbers.add(58);
        numbers.add(65);
        numbers.add(98);
        numbers.forEach((x) -> { System.out.println(x); });
        numbers.forEach(n -> {if (n == 65) {System.out.println("Found" + n);}});
    }
}

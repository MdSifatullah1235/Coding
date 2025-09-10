package WingardiumLeviosa;
import java.util.*;

public class AC {
    public static void main(String[] args) {
        // Initialize a String ArrayList
        ArrayList<String> names = new ArrayList<>();

        // Take few name inputs from users and add them to the list
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of names:");
        int n = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        for (int i = 0; i < n; i++) {
            System.out.println("Enter name " + (i + 1) + ":");
            names.add(scanner.nextLine());
        }

        // Use forEach and lambda to find a particular name
        String targetName = "Eureka";
        names.forEach(name -> {
            if (name.equals(targetName)) {
                System.out.println("Eureka");
            }
        });

        scanner.close();
    }
}

package ExceptionalHandling;
import java.util.Scanner;

public class AC {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Take 2 numbers as input
            System.out.print("Enter first number: ");
            int x = Integer.parseInt(scanner.nextLine());
            System.out.print("Enter second number: ");
            int y = Integer.parseInt(scanner.nextLine());
            
            // Perform division
            int result = x / y;
            System.out.println("Result: " + result);
            
            // Bonus activity: Create an array of 2 items
            int[] arr = new int[2];
            arr[0] = x;
            arr[1] = y;
            
            // Try accessing the 3rd element
            System.out.println("Accessing 3rd element: " + arr[2]);
        } catch (NumberFormatException e) {
            System.out.println("NumberFormatException: Please enter valid integers.");
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException: Division by zero is not allowed.");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBoundsException: Attempted to access an invalid array index.");
        } catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}

package ExceptionalHandling;
import java.util.*;
public class Application {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("------ Try block ------");
            System.out.println("Enter 2 numbers : ");
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = x / y;
            System.out.println(x  + " / " + y + " = " + z);
        } catch (ArithmeticException ex) {
            System.out.println("------ Catch block ------");
            System.out.println(ex.toString());
        } finally {
            System.out.println("------ Finally block ------");
            System.out.println("Application designed and developed by @ Codingal");
            sc.close();
        }
        System.out.println("------ Done ------");
    }
}
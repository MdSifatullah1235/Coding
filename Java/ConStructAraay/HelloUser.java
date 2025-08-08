package Java.ConStructAraay;
import java.util.*;

public class HelloUser {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your name : ");
        String name = sc.nextLine();
        System.out.println( "Enter your lucky number : ");
        int number = sc.nextInt();
        System.out.println("Hello " + name + " your lucky number is " + number);
}
}

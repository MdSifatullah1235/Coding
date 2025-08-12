package Java.ReverseNum;
import java.util.Scanner;

public class ReverseNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number : ");
        for(int i = sc.nextInt(); i > 0; i /= 10) {
            System.out.print("The reverse of " + i + " is " + i % 10);
        }

  
}
}

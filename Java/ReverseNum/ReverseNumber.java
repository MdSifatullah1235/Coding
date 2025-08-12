package Java.ReverseNum;
import java.util.Scanner;

public class ReverseNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int number = sc.nextInt();
        int reversed = 0;

        for (int i = number; i > 0; i /= 10) {
            int digit = i % 10;
            reversed = reversed * 10 + digit;
}

        System.out.println("The reverse number is " + reversed);
        sc.close();
}
}
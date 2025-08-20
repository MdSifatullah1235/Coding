package Inheritance;

import java.util.Scanner;
class Addition {
    void add(int a, int b) {
        System.out.println("Result of Addition: " + (a + b));
    }
}

class Subtraction extends Addition {
    void subtract(int a, int b) {
        System.out.println("Result of Subtraction: " + (a - b));
    }
}

class Multiplication extends Subtraction {
    void multiply(int a, int b) {
        System.out.println("Result of Multiplication: " + (a * b));
    }
}

class Division extends Multiplication {
    void divide(int a, int b) {
        if (b != 0) {
            System.out.println("Result of Division: " + (a / b));
        } else {
            System.out.println("Error! Division by zero not allowed.");
        }
    }
}

public class AC {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Division calc = new Division();

        System.out.print("Enter first number: ");
        int a = sc.nextInt();
        System.out.print("Enter second number: ");
        int b = sc.nextInt();

        System.out.println("\nChoose operation:");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");

        int choice = sc.nextInt();

        switch (choice) {
            case 1:
                calc.add(a, b);
                break;
            case 2:
                calc.subtract(a, b);
                break;
            case 3:
                calc.multiply(a, b);
                break;
            case 4:
                calc.divide(a, b);
                break;
            default:
                System.out.println("Invalid choice!");
        }

        sc.close();
    }
}

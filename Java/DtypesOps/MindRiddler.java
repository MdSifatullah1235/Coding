package Java.DtypesOps;

public class MindRiddler {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        System.out.println("    Guess The Answer    ");
        System.out.println("Unirary Operator : " + a++);
        System.out.println("Unirary Operator : " + ++b);
        System.out.println("Binary Operator : ");
        System.out.println("1 + 2 = " + (1+2));
        System.out.println("1 + 2  = " + 1 + 2);
        System.out.println(1 + 2 + " = 3");
        int increment = ++a * b++;
        System.out.println("Increment : " + increment);
        // uncomment the next lines to know the values
        System.out.println("Current value of a : " + a);
        System.out.println("Current value of b : " + b);
        System.out.println("Tenanary Operator ");
        int largestNumber = (a>b) ? a:b;
        System.out.println("Largest of 2 numbers : " + largestNumber);
    }
}

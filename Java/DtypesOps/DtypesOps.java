package DtypesOps;
public class DtypesOps {
    public static void main(String[] args) {
    int a = 10;
    int b = 5;
    int sum = a + b;
    int diff = a - b;
    int mult = a * b;
    int div = a / b;
    int remainder = a % b;
    String magic = "      Magic      ";
// How to use operators in 2 different methods
    System.out.println("       Method 1       ");
    System.out.println("Addition of a and b = " + sum);
    System.out.println("Difference of a and b = " + diff);
    System.out.println("Multiplication of a and b = " + mult);
    System.out.println("Division of a and b = "+ div);
    System.out.println("Remainder :" + remainder);
    System.out.println("     Method 2    ");
    System.out.println("(2) Addition of a and b = " + (a + b));
    System.out.println("(2) Difference of a and b = " + (a - b));
    System.out.println("(2) Multiplication of a and b = " + (a * b));
    System.out.println("(2) Division of a and b = " + (a / b));
    System.out.println("(2) Remainder : " + (a % b));
    System.out.println(magic);
// The final results
    System.out.println("Addition : " + sum + " Difference : " + diff + " Multiplication : " + mult + " Division : " + div + " Remainder : " + remainder);
  }
}

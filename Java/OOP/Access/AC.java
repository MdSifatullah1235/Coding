package Access;
import java.util.Arrays;
import java.util.Scanner;

public class AC {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the size of the array : ");
    int size = sc.nextInt();
    System.out.print("Enter the "+ size +" elements of the array : ");
    int[] arr = new int[size];
    for (int i = 0; i < size; i++) {
            arr[i] = sc.nextInt();
}
    System.out.println("Array : " + Arrays.toString(arr));
    sc.close();
}
}

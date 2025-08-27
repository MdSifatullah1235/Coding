package Access;
import java.util.Arrays;
import java.util.Scanner;

public class AC {
  public static void mergeSort(int[] arr,int left, int right) {
    if (right > left) {
      int mid = (left + right) / 2;
      mergeSort(arr, left, right);
      mergeSort(arr, mid + 1, right);
      merge(arr, left, mid, right);
    }
  }
  public static void merge(int[] arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int[] la = new int[n1];
    int[] ra = new int[n2];

    for (int i = 0; i < n1; i++) {
      la[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++) {
      ra[j] = arr[mid + 1 + j];
    }
  }
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

import java.util.Scanner;

public class AC {
    String name;
    int[] marks = new int[5];
    String[] subjects = {"Bangla","English","Math","B.G.S","Science"};
    
    Student(){
        System.out.println("*****");
        empno = 101;
        name = "Asish";
        salary = 10000f;
}
    void displaydetails(){
        System.out.println(empno+ " | " + name + " | " + salary);
    }
class Main {
    public static void main(String[] args) {
        Employee emp1 = new Employee();
        Employee emp2 = new Employee();
        Employee emp3 = new Employee();

        emp1.displaydetails();
        emp2.displaydetails();
        emp3.displaydetails();
}
}
}
package Java.OOP;

public class Employee {
    int empno;
    String name;
    float salary;
    
    Employee(){
        System.out.println("*****");
        empno = 101;
        name = "Asish";
        salary = 10000f;
}
    void displaydetails(){
        System.out.println(empno+ " | " + name + " | " + salary);
    }
}

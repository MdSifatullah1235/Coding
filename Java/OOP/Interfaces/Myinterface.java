package Interfaces;

public class Myinterface implements MyInterfaces{
    public void method1() {
        System.out.println("implementation of method1");
    }
    public void method2() {
        System.out.println("implementation of method2");
    }
    public static void main(String[] args) {
        MyInterfaces obj = new Myinterface();
        obj.method1();
        obj.method2();
    }
}


interface MyInterfaces {
    public void method1();
    public void method2();
}
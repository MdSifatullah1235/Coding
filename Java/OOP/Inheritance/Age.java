package Java.OOP.Inheritance;

public class Age {
    static class Main {
        int age;
        Main(int age) {
            this.age = age;
        }
    }

    public static void main(String[] args) {
        Main obj = new Main(24);
        System.out.println("Age : " + obj.age);
    }
}

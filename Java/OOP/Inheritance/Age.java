package Inheritance;

public class Age {
    static class Main {
        int age;
        Main(int age) {
            this.age = age;
        }
    }

    public static void main(String[] args) {
        Age.Main obj = new Age.Main(24);
        System.out.println("Age : " + obj.age);
    }
}
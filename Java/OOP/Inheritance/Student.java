package Inheritance;
public class Student {
    static class Parent {
        int age, id;
        String name;
        void naming(String name) {
            System.out.println("My name is " + name);
        }
    }
    static class Child extends Parent {
        void ageN(int age) {
            System.out.println("My age is " + age);
        }
    }
    static class Main {
        public static void main(String[] args) {
            Child s = new Child();
            s.naming("Sifat");
            s.ageN(14);
        }
    }
}
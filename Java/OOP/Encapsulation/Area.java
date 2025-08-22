package Encapsulation;

public class Area {
    public static void main(String[] args) {
        Shape[] shape = new Shape[2];
        shape[0] = new Triangle(2, 2);
        shape[1] = new Square(4);
        System.out.println("Area of triangle is " + shape[0].getArea());
        System.out.println("Area of square is " + shape[1].getArea());
    }
}

class Shape {
    public double getArea() {
        return 0;
    }
}

class Triangle extends Shape {
    private double base, height;
    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }
    public double getArea() {
        return 0.5 * base * height;
    }
}

class Square extends Shape {
    private double side;
    public Square(double side) {
        this.side = side;
    }
    public double getArea() {
        return side * side;
    }
}

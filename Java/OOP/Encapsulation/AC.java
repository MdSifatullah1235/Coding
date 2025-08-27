package Encapsulation;

public class AC {
    public static void main(String[] args) {
        Cube cube = new Cube(2, 2, 2);
        Cuboid cuboid = new Cuboid(2, 2, 2);
        Cylinder cylinder = new Cylinder(2, 2);
        Trianguler trianguler = new Trianguler(2, 2, 2);
        System.out.println(cube.getVolume());
        System.out.println(cuboid.getVolume());
        System.out.println(cylinder.getVolume());
        System.out.println(trianguler.getVolume());
    }
}

class Shape {
    public double getVolume() {
        return 0;
    }
}

class Cube extends Shape {
    private double length, width, height;
    public Cube(double length, double width, double height) {
        this.length = length;
        this.width = width;
        this.height = height;
    }
    public double getVolume() {
        return length * width * height;
    }
}

class Cuboid extends Shape {
    private double length, breadth, height;
    public Cuboid(double length, double breadth, double height) {
        this.length = length;
        this.breadth = breadth;
        this.height = height;
    }
    public double getVolume() {
        return length * breadth * height;
    }
}

class Cylinder extends Shape {
    private double radius, height;
    public Cylinder(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }
    public double getVolume() {
        return 3.14 * radius * radius * height;
    }
}

class Trianguler extends Shape {
    private double baseEdge, height, length;
    public Trianguler(double baseEdge, double height, double length) {
        this.baseEdge = baseEdge;
        this.height = height;
        this.length = length;
    }
    public double getVolume() {
        return 0.5 * baseEdge * height * length;
    }
}
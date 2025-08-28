package Encapsulation;

public class AC {
    public static void main(String[] args) {
        Cube cube = new Cube(2, 2, 2);
        Cuboid cuboid = new Cuboid(2, 2, 2);
        Cylinder cylinder = new Cylinder(2, 2);
        Trianguler trianguler = new Trianguler(2, 2, 2);
        Cone cone = new Cone(2, 2);
        Sphere sphere = new Sphere(2);
        System.out.println("Volume of a Cube : " + cube.getVolume());
        System.out.println("Volume of a Cuboid : " + cuboid.getVolume());
        System.out.println("Volume of a Cylinder : " + cylinder.getVolume());
        System.out.println("Volume of a Trianguler : " + trianguler.getVolume());
        System.out.println("Volume of a Cone : " + cone.getVolume());
        System.out.println("Volume of a Sphere : " + sphere.getVolume());
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

class Cone extends Shape {
    private double radius, perpendicularHeight;
    public Cone(double radius, double height) {
        this.radius = radius;
        this.perpendicularHeight = height;
    }
    public double getVolume() {
        return 0.33 * 3.14 * radius * radius * perpendicularHeight;
    }
}

class Sphere extends Shape {
    private double radius;
    public Sphere(double radius) {
        this.radius = radius;
    }
    public double getVolume() {
        return 1.33 * 3.14 * radius * radius * radius;
    }
}
package PolymorphismAbstraction;

public class Objects {
    public static void main(String[] args) {
        
    }
}

abstract class Object_s {
    abstract void show_shape();
    public void shape() {
        System.out.println("Im from a abstract class");
    }
}


class Sphere extends Object_s {
    public void show_shape() {
        System.out.println("Object type is Sphere");
    }
}

class Cuboid extends Object_s {
    public void show_shape() {
        System.out.println("Object type is Cuboid");
    }
}

class Prism extends Object_s {
    public void show_shape() {
        System.out.println("Object type is Prism");
    }
}
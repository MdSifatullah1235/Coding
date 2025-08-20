package Inheritance;
public class Mammals {
    void mam() {
        System.out.println("Inside Mammals Class");
    }
}

class Lion extends Mammals {
    void roar(){
        System.out.println("Inside Lion CLass");
    }
}

class Human extends Mammals{
    void speak(){
        System.out.println("Inside Human Class");
    }
}


class Main {
    public static void main(String[] args) {
        Lion obj = new Lion();
        obj.mam();
        obj.roar();
        //obj.speak(); error
        Human obj2 = new Human();
        obj2.mam();
        obj2.speak();
    }
}
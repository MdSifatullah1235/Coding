package Java.OOP.Inheritance;

public class Animal {
    void eat(){
        System.out.println("eating... Animal class.... eta method");
    }

}

class Lion extends Animal {
    void roar(){
        System.out.println("Roaring... Lion class... roar method");
    }
}

class babyLion extends Lion {
    void weep(){
        System.out.println("weeping... babyLion class... weep method");
    }
}

class Main {
   public static void main(String[] args) {
       babyLion obj = new babyLion();
       obj.eat();
       obj.roar();
       obj.weep();
   } 
}
package Access;

public class Main {
    public static void main(String[] args) {
        Parent p = new Child();
        // Parent p2 = new Parent();
        p.display();
        //p2.display();
    }
}


class Parent {
    public void display() {
        System.out.println("Parent Class");
    }
}

class Child extends Parent {
    @Override
    public void display() {
        System.out.println("Child Class");
    }
}
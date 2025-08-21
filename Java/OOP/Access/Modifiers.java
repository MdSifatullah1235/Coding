package Access;

public class Modifiers {
    public static void main(String[] args) {
        Child obj = new Child();
        obj.protect();
        // obj.priv();

        System.out.println("Hello World!");
    }
}

class Parent {
    protected void protect() 
    {
        System.out.println("inside the protected method");
    }
}

class Child extends Parent {
    private void priv() 
    {
        System.out.println("inside the private method");
    }
}
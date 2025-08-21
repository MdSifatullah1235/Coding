package Access;

public class Super {
    public static void main(String[] args) {
        subclass obj = new subclass();
        obj.display();
    }
}


class supersclass {
    int number = 10;
}


class subclass extends supersclass {
    int number = 20;
    void display() {
        System.out.println(number);
        System.out.println(super.number);
    }
}
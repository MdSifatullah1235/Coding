package Interfaces;

public class Vehicles {
    public static void main(String[] args) {
        Bicycle bicycle = new Bicycle();
        bicycle.changeGear(2);
        bicycle.speedUp(3);
        bicycle.applyBrakes(1);

        System.out.println("The present state of bicycle : ");
        bicycle.printStates();

        Car car = new Car();
        car.changeGear(1);
        car.speedUp(4);
        car.applyBrakes(3);

        System.out.println("The present state of car : ");
        car.printStates();
    }
}

interface Vehicle {
    void changeGear(int a);
    void speedUp(int a);
    void applyBrakes(int a);
}

class Bicycle implements Vehicle {
    int speed;
    int gear;

    @Override
    public void changeGear(int newGear) {
        gear = newGear;
    }

    @Override
    public void speedUp(int increment) {
        speed += increment;
    }

    @Override
    public void applyBrakes(int decrement) {
        speed -= decrement;
    }

    public void printStates() {
        System.out.println("Speed: " + speed);
        System.out.println("Gear: " + gear);

    }

}

class Car implements Vehicle {
    int speed;
    int gear;
    @Override
    public void changeGear(int newGear) {
        gear = newGear;
    }
    @Override
    public void speedUp(int increment) {
        speed += increment;
    }
    @Override
    public void applyBrakes(int decrement) {
        speed -= decrement;
    }

    public void printStates() {
        System.out.println("Speed: " + speed);
        System.out.println("Gear: " + gear);

    }
}
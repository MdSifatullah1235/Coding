package Interfaces;
import java.util.*;
public class AC 

{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the speedup value of the bike : ");
        int sunum= sc.nextInt();
        System.out.println("Enter the changeGear value of the bike : ");
        int cgnum = sc.nextInt();
        System.out.println("Enter the applyBrakes value of the bike : ");
        int abnum = sc.nextInt();

        Bike bicycle = new Bike();
        bicycle.changeGear(cgnum);
        bicycle.speedUp(sunum);
        bicycle.applyBrakes(abnum);

        System.out.println("The present state of bicycle : ");
        bicycle.printStates();

        System.out.println("Enter the speedup value of the truck : ");
        int sunum1= sc.nextInt();
        System.out.println("Enter the changeGear value of the truck : ");
        int cgnum1 = sc.nextInt();
        System.out.println("Enter the applyBrakes value of the truck : ");
        int abnum1 = sc.nextInt();

        Truck truck = new Truck();
        truck.changeGear(cgnum1);
        truck.speedUp(sunum1);
        truck.applyBrakes(abnum1);

        System.out.println("The present state of truck : ");
        truck.printStates();
        sc.close();
    }
}

interface Vehicle {
    void changeGear(int a);
    void speedUp(int a);
    void applyBrakes(int a);
}

class Bike implements Vehicle {
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

class Truck implements Vehicle {
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
package PolymorphismAbstraction;

public class Hillstation {
    public static void main(String[] args) {
        HillStations A = new HillStations();
        HillStations N = new Nilgiri();
        HillStations K = new Keokradon();
        HillStations Na = new Nilachal();
        HillStations Z = new ZowTlang();
        A.location();
        A.famousfor();
        N.location();
        N.famousfor();
        K.location();
        K.famousfor();
        Na.location();
        Na.famousfor();
        Z.location();
        Z.famousfor();
    }
}

class HillStations {
    void location() {
        System.out.println("location");
    }

    void famousfor(){
        System.out.println("famous for");
    }
}


class Nilgiri extends HillStations {
    void location() {
        System.out.println("Nilgiri is in Chittagong");
    }

    void famousfor(){
        System.out.println("its stunning natural beauty,cloud-kissed peaks, lush green hills, and a serene atmosphere");
    }
}


class Keokradon extends HillStations {
    void location() {
        System.out.println("Keokradon is in Chittagong");
    }

    void famousfor(){
        System.out.println("its scenic beauty, dense forests, tribal life, and nearby attractions");
    }
}

class Nilachal extends HillStations {
    void location() {
        System.out.println("Nilachal is in Chittagong");
    }

    void famousfor(){
        System.out.println("its breathtaking scenic beauty, with stunning views of clouds and mist from a high altitude");
    }
}

class ZowTlang extends HillStations {
    void location() {
        System.out.println("Zow Tlang is in Chittagong");
    }

    void famousfor(){
        System.out.println("being one of the country's highest and wildest mountain peaks, offering a difficult challenge to trekkers and adventurers");
    }
}
package PolymorphismAbstraction;

public class AC {
    public static void main(String[] args) {
        SevenWonders sw = new SevenWonders();
        sw.name();
        TajMahal tm = new TajMahal();
        tm.name();
        GreatWallOfChina gwc = new GreatWallOfChina();
        gwc.name();
        ChristTheRedeemer ctr = new ChristTheRedeemer();
        ctr.name();
        MachuPicchu mp = new MachuPicchu();
        mp.name();
        ChichenItza ci = new ChichenItza();
        ci.name();
        Colosseum co = new Colosseum();
        co.name();
        Petra p = new Petra();
        p.name();

        sw.location();
        tm.location();
        gwc.location();
        ctr.location();
        mp.location();
        ci.location();
        co.location();
        p.location();
    }
}


class SevenWonders {
 void name() {
    System.out.println("----------- The Seven Wonders of the World -----------");
 }

 void location() {
    System.out.println("----------- Their locations ------------");
 }
}


class TajMahal extends SevenWonders {
 void name() {
    System.out.println("Taj Mahal");
 }
 void location(){
    System.out.println("India");
 } 
}

class GreatWallOfChina extends SevenWonders {
 void name() {
    System.out.println("Great Wall of China");
 }
 void location(){
    System.out.println("China");
 } 
}

class ChristTheRedeemer extends SevenWonders {
 void name() {
    System.out.println("Christ the Redeemer");
 }
 void location(){
    System.out.println("Brazil");
 } 
}

class MachuPicchu extends SevenWonders {
 void name() {
    System.out.println("Machu Picchu");
 }
 void location(){
    System.out.println("Peru");
 } 
}

class ChichenItza extends SevenWonders {
 void name() {
    System.out.println("Chichen Itza");
 }
 void location(){
    System.out.println("Mexico");
 } 
}

class Colosseum extends SevenWonders {
 void name() {
    System.out.println("Colosseum");
 }
 void location(){
    System.out.println("Italy");
 } 
}

class Petra extends SevenWonders {
 void name() {
    System.out.println("Petra");
 }
 void location(){
    System.out.println("Jordan");
 } 
}
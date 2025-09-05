package WingardiumLeviosa;
import java.util.*;
public class Magic1 {
    public static void main(String[] args) {
        // ArrayList
        ArrayList<String> animals = new ArrayList<>();
        // added 3 elements
        animals.add("Lion");
        animals.add("Cheetah");
        animals.add("Tiger");
        System.out.println("=========== Printing Current List ============");
        System.out.println(animals);
        animals.clear();
        System.out.println("=========== Printing Cleared List ============");
        System.out.println("Empty list : " + animals);
        if(animals.isEmpty()){
            System.out.println("Array is empty");
        }
        else{
            System.out.println("Array is not empty");
        }

        animals.add("Lion");
        animals.add("Cheetah");
        animals.add("Tiger");

        System.out.println("Size of the array : " + animals.size());
        System.out.println("Adding more elements to the array : " + animals.add("Horse") + " " + animals.add("Elephant"));
        System.out.println(animals);
        animals.remove(2);
        System.out.println(animals);
    }
}
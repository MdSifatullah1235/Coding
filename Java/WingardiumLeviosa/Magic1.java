package WingardiumLeviosa;
import java.util.*;
public class Magic1 {
    public static void main(String[] args) {
        // ArrayList
        ArrayList<String> animals = new ArrayList<>();
        // Adding elements
        animals.add("Lion");
        animals.add("Cheetah");
        animals.add("Tiger");
        System.out.println("=========== Printing Current List ============");
        System.out.println(animals);
        // Cleared the array
        animals.clear();
        System.out.println("=========== Printing Cleared List ============");
        System.out.println("Empty list : " + animals);
        // Writing a if else statement to see if the array is empty or not
        if(animals.isEmpty()){
            System.out.println("Array is empty");
        }
        else{
            System.out.println("Array is not empty");
        }
        // Adding elements to the empty array
        animals.add("Lion");
        animals.add("Cheetah");
        animals.add("Tiger");

        System.out.println("Size of the array : " + animals.size());
        System.out.println("Adding more elements to the array : " + animals.add("Horse") + " " + animals.add("Elephant"));
        System.out.println(animals);
        // Removed the 3rd element
        animals.remove(2);
        System.out.println(animals);
    }
}
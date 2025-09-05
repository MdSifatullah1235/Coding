package WingardiumLeviosa;
import java.util.*;
public class Magic1 {
    public static void main(String[] args) {
        ArrayList<String> animals = new ArrayList<>();

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
    }
}
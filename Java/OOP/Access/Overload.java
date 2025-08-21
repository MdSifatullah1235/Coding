package Access;

public class Overload {
    public static void main(String[] args) {
        Student s1 = new Student();
        Student s2 = new Student(30, "Sifat");
        Student s3 = new Student(10, "Musfiq", 1000);

        s1.displayDetails();
        s2.displayDetails();
        s3.displayDetails();
    }
}

class Student {
    int id;
    String name;
    float stipend;

    Student() {}

    Student(int id, String name) {
        this.id = id;
        this.name = name;
    }

    Student(int id, String name, float stipend) {
        this.id = id;
        this.name = name;
        this.stipend = stipend;

    }

    void displayDetails(){
        System.out.println(id + " | " + name + " | " + stipend);
    }
}
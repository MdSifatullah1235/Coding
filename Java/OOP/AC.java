import java.util.Scanner;

public class AC {
    String name;
    int[] marks = new int[5];
    String[] subjects = {"Bangla","English","Math","B.G.S","Science"};
    
    void Student(){
        System.out.println("*****");
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your name : ");
        name = sc.nextLine();
        for (int i = 0; i < 5; i++) {
            System.out.print("Enter marks of " + subjects[i] + " : ");
            marks[i] = sc.nextInt();
        }
        sc.close();
}
    void ReportCard(){
        System.out.println("------------------");
        System.out.println("Report Card");
        System.out.println("Name : " + name);
        System.out.println("------------------");
        System.out.println("Subject      Marks");
        System.out.println("------------------");
        for (int i = 0; i < 5; i++) {
            System.out.println(subjects[i] + " : " + marks[i]);
        }

        System.out.println("------------------");
        System.out.println("Total Marks : " + (marks[0] + marks[1] + marks[2] + marks[3] + marks[4]) + "Average : " + (marks[0] + marks[1] + marks[2] + marks[3] + marks[4])/5);

    }
}
package Java.ConStructAraay;
import java.util.Scanner;

import Java.ConStructAraay.*;
public class GradingSytem {
    public static void main(String[] args) {
        int sum = 0;
        String result;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of subjects : ");
        int noOfSubs = sc.nextInt();
        int marks[] = new int[noOfSubs];
        System.out.println("Enter the marks of "+ noOfSubs + " subjects. Press enter to give marks for another subject : ");
        for(int i = 0; i < noOfSubs; i++) {
            marks[i] = sc.nextInt();
        
}
for(int j =0; j < noOfSubs; j ++) {
    sum += marks[j];
}

int percentage = sum / noOfSubs;
System.out.println("Your percentage is " + percentage + "%");
if (percentage >= 95){
    result = "Your grade is A+";
}
else if (percentage >= 90) {
    result = "Your grade is A";
}
else if (percentage >= 85) {
    result = "Your grade is B+";
} 
else if (percentage >= 80) {
    result = "Your grade is B";
} 
else if (percentage >= 75) {
    result = "Your grade is C+";
} 
else if (percentage >= 70) {
    result = "Your grade is C";
} 
else if (percentage >= 65) {
    result = "Your grade is D+";
} 
else if (percentage >= 60) {
    result = "Your grade is D";
} 
else if (percentage >= 55) {
    result = "Your grade is F+";
}
else if (percentage >= 50) {
    result = "Your grade is F";
}
else {
    result = "You failed";
}

System.out.println(result);
}
}

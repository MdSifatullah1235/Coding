package Java.LeapYearChecker;

public class Code {
    public static void main(String[] args) {
        int year = 1900;
        String checker = (year % 4 == 0 && (year % 100 != 0)) ? "This is a leap year" : "This is not a leap year";
        System.out.println(checker);
    }
}
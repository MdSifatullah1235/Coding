package LeapYearChecker;
/* Just a program to check 
if a year assigned to the "year" variable
is a leap year or not
*/

public class Code {
    public static void main(String[] args) {
        System.out.println("========= Leap Year Checker =========");
        int year = 2048;
        System.out.println("Year = " + year);
        String checker = (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) ? year + " is a leap year" : year + " is not a leap year";
        System.out.println(checker);
    }
}
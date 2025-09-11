package BankingApplication;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        boolean infiniteLoop = true;
        double[] accountBalance = new double[1000];
        String[] accountName = new String[1000];
        int option, size = 100;
        while (infiniteLoop) {
            System.out.println("Welcome to Codingal Banking Services");
            System.out.println("Banking Menu :");
            System.out.println("1 -> Add Account");
            System.out.println("2 -> Change Customer Name");
            System.out.println("3 -> Check Account Balance");
            System.out.println("4 -> Update Account Balance");
            System.out.println("5 -> Summary of All Accounts");
            System.out.println("6 -> Exit");
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your option : ");
        option = sc.nextInt();

        if (option == 1) {
            System.out.println("\n Add Customer \n Menu ->");
            sc.nextLine();

            System.out.print("\nEnter Customer Name : ");
            String name = sc.nextLine();
            accountName[size] = name;

            System.out.println("Enter Opening Balance : ");
            double amt = sc.nextDouble();
            accountBalance[size] = amt;

            System.out.println("\nAccount Created Successfully\n");
            System.out.println("Name : " + name);
            System.out.println("Opening Balance : " + amt);
            System.out.println("Account Number : " + (size));
            System.out.println("Account Name : " + accountName[size]);
            System.out.println("Account Balance : " + accountBalance[size] +" taka");

            System.out.println("========================");

            size = size + 1;
        }

        else if (option == 2) {
            System.out.println("\n Change Customer Name \n Menu ->");
            System.out.print("\n Enter Account Number : ");

            int accountIndex;
            String temp;

            accountIndex = sc.nextInt();
            sc.nextLine();

            if (accountIndex > size) {
                System.out.println("Invalid Account Number");
                System.out.println("Terminating");
            }
            
            else {
                temp = accountName[accountIndex];
                System.out.println("Enter new name : ");
                String name = sc.nextLine();
                accountName[accountIndex] = name;
                System.out.println("Name is successfully updated from " + temp + " to " + name);
            }

            System.out.println("========================");

        } else if (option == 3) {
            System.out.println("\n Check Account Balance \n Menu ->");
            System.out.println("Enter Account Number : ");
            
            int accountIndex;
            accountIndex = sc.nextInt();
            if (accountIndex > size ) {
                System.out.println("Account Does Not Exist");
                System.out.println("Terminating");
            }
            else {
                System.out.println("Account Name : " + accountName[accountIndex]);
                System.out.println("Account Balance : " + accountBalance[accountIndex] + " taka");
            }
        }
        else if (option == 4) {
            System.out.println(
                "\n Update Account Balance \n Menu ->"
            );

            System.out.println("Enter Account Number : ");
            int accountIndex;
            accountIndex = sc.nextInt();

            if (accountIndex > size) {
                System.out.println("Account Does Not Exist");
                System.out.println("Terminating");
            }

            else {
                System.out.println("Enter the amount to be deposited : ");
                double amt = sc.nextDouble();

                accountBalance[accountIndex] += amt;

                System.out.println("Your updated account balance is " + accountBalance[accountIndex] + " taka");

            }
        System.out.println("========================");
            }

        else if (option == 5) {
            System.out.println("\n Summary of All Accounts \n Menu ->");
            System.out.println("Accounts Registered : ");
            for (int i = 100; i > 0; i--) {
                System.out.println("Account Number : " + i);
                System.out.println("Account Name : " + accountName[i]);
                System.out.println("Account Balance : " + accountBalance[i] + " taka");
            }
        } else if (option == 6) {
            System.out.println("Terminating");
            infiniteLoop = false;
        } else {
            System.out.println("Invalid Option");
            System.out.println("Terminating");
            infiniteLoop = false;
        }
    
    }

}
}
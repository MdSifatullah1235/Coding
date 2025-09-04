package ExceptionalHandling;

import java.util.*;

public class InternHiring {
    public static Candidate getCandidateDetails() throws InvalidInternException {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Candidate Details: ");
        System.out.println("Name");
        String name = sc.nextLine();
        System.out.println("Gender");
        String gender = sc.nextLine();
        System.out.println("Enter percentage in 10th");
        int percentage = sc.nextInt();
        if (percentage < 50) {
            throw new InvalidInternException("Registration Unsuccessful");
        } else {
            Candidate candidate = new Candidate();
            candidate.setName(name);
            candidate.setGender(gender);
            candidate.setPercentage(percentage);
            return candidate;
        }

    }

    public static void main(String[] args) {
        System.out.println("Welcome to Intern Hiring Tool");
        try {
            Candidate candidate = getCandidateDetails();
            System.out.println("Registration Successful");
        } catch (InvalidInternException e) {
            System.out.println(e.getMessage());
        }
    }

    public static class Candidate {
        private String name;
        private String gender;
        private int percentage;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getGender() {
            return gender;
        }

        public void setGender(String gender) {
            this.gender = gender;
        }

        public int getPercentage() {
            return percentage;
        }

        public void setPercentage(int percentage) {
            this.percentage = percentage;
        }
    }
}

class InvalidInternException extends Exception {
    public InvalidInternException(String message) {
        super(message);
    }
}
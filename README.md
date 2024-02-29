# Malicious-URL-Detector-Using-Classification-and-Regression-Trees



import java.util.Scanner;

public class LeapYearChecker {
    public static void main(String[] args) {
        System.out.println("Name : Aditya Singh ");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a year: ");
        int year = scanner.nextInt();

        if (isLeapYear(year)) {
            System.out.println(year + " is a leap year.");
        } else {
            System.out.println(year + " is not a leap year.");
        }

        scanner.close();
    }

    public static boolean isLeapYear(int year) {
        // Leap year is divisible by 4
        // If divisible by 100, also divisible by 400
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }
}






import java.util.Scanner;

public class VowelConsonantChecker {
    public static void main(String[] args) {
          System.out.println("Name : Aditya Singh ");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a character: ");
        char ch = scanner.next().charAt(0);

        if (isVowel(ch)) {
            System.out.println(ch + " is a vowel.");
        } else {
            System.out.println(ch + " is a consonant.");
        }

        scanner.close();
    }

    public static boolean isVowel(char ch) {
        ch = Character.toLowerCase(ch);
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
}








import java.util.Scanner;

public class VariableSwapper {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the first number: ");
        int a = scanner.nextInt();
        
        System.out.print("Enter the second number: ");
        int b = scanner.nextInt();
        
        System.out.println("Before swapping: a = " Screenshot from 2024-02-29 14-16-49+ a + ", b = " + b);
        
        // Swapping without third variable using arithmetic operations
        a = a + b;
        b = a - b;
        a = a - b;
        
        System.out.println("After swapping: a = " + a + ", b = " + b);
        
        scanner.close();
    }
}








import java.util.Scanner;

public class LargestOfThree {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
               System.out.println("Name : Aditya Singh ");
        
        System.out.println("Enter three numbers:");
        double num1 = scanner.nextDouble();
        double num2 = scanner.nextDouble();
        double num3 = scanner.nextDouble();
        
        double largest = findLargest(num1, num2, num3);
        
        System.out.println("The largest number is: " + largest);
        
        scanner.close();
    }
    
    public static double findLargest(double num1, double num2, double num3) {
        if (num1 >= num2 && num1 >= num3) {
            return num1;
        } else if (num2 >= num1 && num2 >= num3) {
            return num2;
        } else {
            return num3;
        }
    }
}



![image](https://github.com/PranavBarthwal/Malicious-URL-Detector-Using-Classification-and-Regression-Trees/assets/110532770/12f04f6f-3e8d-4937-a109-f8e3c2dab509)

![image](https://github.com/PranavBarthwal/Malicious-URL-Detector-Using-Classification-and-Regression-Trees/assets/110532770/a1851f65-0fbc-49b9-99e7-e49ac0c33850)

![image](https://github.com/PranavBarthwal/Malicious-URL-Detector-Using-Classification-and-Regression-Trees/assets/110532770/8a8f20d1-89ff-4317-a628-11591ae7d825)

![image](https://github.com/PranavBarthwal/Malicious-URL-Detector-Using-Classification-and-Regression-Trees/assets/110532770/e8598a30-6b9c-478b-9b0d-14c536d8d7d5)

![image](https://github.com/PranavBarthwal/Malicious-URL-Detector-Using-Classification-and-Regression-Trees/assets/110532770/a1983385-269b-4f59-b553-4175cfe12acc)

![image](https://github.com/PranavBarthwal/Malicious-URL-Detector-Using-Classification-and-Regression-Trees/assets/110532770/c07921dd-8a89-46e5-b679-8a1255af1c2e)

![image](https://github.com/PranavBarthwal/Malicious-URL-Detector-Using-Classification-and-Regression-Trees/assets/110532770/73a7d85a-f260-4a64-a5b7-abad6aab2dd9)

![image](https://github.com/PranavBarthwal/Malicious-URL-Detector-Using-Classification-and-Regression-Trees/assets/110532770/cd6b054e-a726-4fd9-8bc2-9ff102491f02)





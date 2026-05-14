import java.util.*;

public class Main {
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        int a, b, ch;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a: ");
        a = sc.nextInt();

        System.out.print("Enter b: ");
        b = sc.nextInt();

        System.out.println("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVIDE");
        ch = sc.nextInt();

        switch (ch) {
            case 1 -> {
                Addition add = new Addition();
                System.out.println("Result: " + add.calculate(a, b));
            }

            case 2 -> {
                Subtraction sub = new Subtraction();
                System.out.println("Result: " + sub.calculate(a, b));
            }

            case 3 -> {
                Multiplication mul = new Multiplication();
                System.out.println("Result: " + mul.calculate(a, b));
            }

            case 4 -> {
                Divide div = new Divide();
                System.out.println("Result: " + div.calculate(a, b));
            }

            default -> System.out.println("Invalid choice");
        }

        sc.close();
    }
}

class Addition {
    int calculate(int a, int b) {
        return a + b;
    }
}

class Subtraction {
    int calculate(int a, int b) {
        return a - b;
    }
}

class Multiplication {
    int calculate(int a, int b) {
        return a * b;
    }
}

class Divide {
    int calculate(int a, int b) {
        if (b == 0) {
            System.out.println("Cannot divide by zero");
            return 0;
        }
        return a / b;
    }
}

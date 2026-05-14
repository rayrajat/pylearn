import java.util.*;

class GreatestOfAllThree {
    public static void main(String args[]) {
        @SuppressWarnings("resource")
        Scanner obj = new Scanner(System.in); // One scanner is enough
        
        System.out.print("Enter value of a: ");
        int a = obj.nextInt();
        
        System.out.print("Enter value of b: ");
        int b = obj.nextInt();
        
        System.out.print("Enter value of c: ");
        int c = obj.nextInt();
        
        if (a > b && a > c) {
            System.out.print(a + " is greatest among all");
        } 
        else if (b > a && b > c) {
            System.out.print(b + " is greatest among all");
        } 
        else if (c > a && c > b) {
            System.out.print(c + " is greatest among all");
        } 
        else {
            System.out.print("There is a tie or all are equal");
        }
    }
}


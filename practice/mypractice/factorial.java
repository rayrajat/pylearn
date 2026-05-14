import java.math.BigInteger;
import java.util.*; // Required for massive numbers

class Factorial {
    public static void main(String args[]) {
        @SuppressWarnings("resource")
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter value: ");
        int num = obj.nextInt();
        
        // Start with BigInteger "1"
        BigInteger fact = BigInteger.ONE;
        
        for (int i = num; i > 0; i--) {
            // BigInteger requires using methods like .multiply() instead of *
            fact = fact.multiply(BigInteger.valueOf(i));
        }
        
        System.out.print("Factorial of " + num + " is: \n" + fact);
    }
}

/*The reason you're seeing 0 (or negative numbers) is because an int in Java can only hold a maximum value of about 2.1 billion (

).
Factorials grow incredibly fast. Even 13! exceeds the limit of an int, and 21! exceeds the limit of a long. For numbers like 70 or 98, the result has over 100 digits, which causes the bits to "overflow" until they cycle back to zero.
To handle massive numbers like 

, you must use the BigInteger class from java.math.
 */

/*Why this works:
BigInteger: It has no fixed limit; it will use as much memory as needed to store the full number.
BigInteger.valueOf(i): Converts your loop integer into a BigInteger so they can be multiplied together.
.multiply(): Since BigInteger is an object, you can't use the * symbol; you use the method instead.
 */
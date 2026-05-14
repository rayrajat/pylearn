import java.util.*;
class powernum {
    public static void main(String args[]){
        int num;
        int power;
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter value:");
        num = obj.nextInt();
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter power value:");
        power = ob.nextInt();
        
        System.out.print("power of "+num+" is "+Math.pow(num,power));
        
        obj.close();
        ob.close();
    }
}
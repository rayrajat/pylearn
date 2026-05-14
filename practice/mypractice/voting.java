import java.util.*;
class voting{
    public static void main(String args[]){
        int age;
        Scanner obj = new Scanner(System.in);
        System.out.print("enter the age of voter:");
        age = obj.nextInt();
        
        if(age>18||age==18){
            System.out.print("Eligible to vote.");
        }
        else{
            System.out.print("Not eligible to vote.");
        }

        obj.close();
    }
}

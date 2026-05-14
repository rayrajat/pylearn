import java.util.*;
class tax{
    public static void main(String args[]){
        int salary;
        @SuppressWarnings("resource")
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter your salary:");
        salary = obj.nextInt();
        
        if(salary<=10000){
            System.out.print("No tax");
        }
        else if(salary>10000&&salary<=100000){
            System.out.print("total tax to be paid is:"+(0.10*salary));
            
        }
        else{
            System.out.print("total tax to be paid:"+(0.20*salary));
        }
    }
}

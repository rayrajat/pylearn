import java.util.*;
class addition{
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String args[]){
        int a;int b;
        Scanner obj=new Scanner(System.in);
        System.out.print("enter value of first integer:");
        a=obj.nextInt();
        obj.close();
        Scanner ob=new Scanner(System.in);
        System.out.print("enter value of second integer:");
        b=ob.nextInt();
        
        System.out.print("sum of two number is :"+(a+b));
        
        ob.close();
    }  
}

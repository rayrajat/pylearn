import java.util.*;
class great{
    public static void main(String args[]){
        int a; int b; 
        @SuppressWarnings("resource")
        Scanner obj = new Scanner(System.in);
        System.out.print("enter value of a:");
        a=obj.nextInt();
        @SuppressWarnings("resource")
        Scanner ob = new Scanner(System.in);
        System.out.print("enter value of b:");
        b=ob.nextInt();
        
        if(a>b){
            System.out.print(+a+"is greater than"+b);
        }
        else{
            System.out.print(+b+" is greater than "+a);
        }
    }
}

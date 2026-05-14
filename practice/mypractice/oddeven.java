import java.util.*;
class oddeven{
    public static void main(String args[]){
        int a;
        @SuppressWarnings("resource")
        Scanner obj = new Scanner(System.in);
        System.out.print("enter integer value:");
        a=obj.nextInt();
        if(a%2==0){
            System.out.print("even");
        }
        else{
            System.out.print("odd");
        }
    }
}

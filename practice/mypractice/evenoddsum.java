import java.util.*;
class evenoddsum{
    public static void main(String args[]){
        int n;int total=0;
        @SuppressWarnings("resource")
        Scanner obj = new Scanner(System.in);
        System.out.print("enter value:");
        n=obj.nextInt();
        for(int i=n;i>=0;i-=2){
            total+=i;
        }
        if(n%2==0){
            System.out.print("sum of all even numbers:"+total);
        }
        else{
            System.out.print("sum of all odd numbers:"+total);
        }
        
    }
}

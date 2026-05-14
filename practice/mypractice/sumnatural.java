import java.util.*;
class sumnatural{
    public static void main(String args[]){
        int a;int total=0;
        @SuppressWarnings("resource")
        Scanner obj=new Scanner(System.in);
        System.out.print("enter value upto which natural number want?:");
        a=obj.nextInt();
        for(int i=1 ;i<=a;i++){
            total=total+i;
        }
        System.out.print("sum of first n natural number:"+(total));
        
    }
}

import java.util.*;
class  natural{
    public static void main(String args[]){
        int a;
        @SuppressWarnings("resource")
        Scanner obj=new Scanner(System.in);
        System.out.print("enter value upto which natural number want?:");
        a=obj.nextInt();
        for(int i=1 ;i<=a;i++){
            System.out.println("natural number upto a:"+i);
        }
        
    }
}

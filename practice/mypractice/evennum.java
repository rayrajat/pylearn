import java.util.*;
class even{
    public static void main(String args[]){
        int n;int total=0;
        @SuppressWarnings("resource")
        Scanner obj = new Scanner(System.in);
        System.out.print("enter number:");
        n=obj.nextInt();
        for(int i=0;i<=n;i++){
            if(i%2==0){
                 total=total+i;
            }
           
        }
        System.out.print("total sum of n numbers:"+total);
    }
}

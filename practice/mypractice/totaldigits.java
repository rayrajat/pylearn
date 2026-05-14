import java.util.*;
class totaldigits{
    public static void main(String args[]){
        int count=0;int n;
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter num:");
        n=obj.nextInt();
        while(n>0){
            n=n/10;
            count++;
        }
        System.out.print("total number of digits:"+count);
        obj.close();
    }
}
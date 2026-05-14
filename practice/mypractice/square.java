import java.util.*;
class power{
    public static void main(String args[]){
        int n;
        @SuppressWarnings("resource")
        Scanner obj = new Scanner(System.in);
        System.out.print("enter value :");
        n = obj.nextInt();
        for(int i=0;i<=n;i++){
            System.out.print("power of "+i+" is "+(i*i)+"\n");
        }
    }
}

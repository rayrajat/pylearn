import java.util.*;
class oddnumber{
    public static void main(String args[]){
        int n;
        @SuppressWarnings("resource")
        Scanner obj = new Scanner(System.in);
        System.out.print("enter value:");
        n=obj.nextInt();
        for(int i=0;i<=n;i++){
            if(i%2!=0){
                System.out.print("odd number:"+i+"\n");
            }
        }
    }
}

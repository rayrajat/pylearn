import java.util.*;
class evenodd{
    public static void main(String args[]){
        int n;int totaleven=0;int totalodd=0;
        @SuppressWarnings("resource")
        Scanner obj = new Scanner(System.in);
        System.out.print("Enter num");
        n=obj.nextInt();
        for(int i=0;i<=n;i++){
            if(i%2!=0){
                totalodd=totalodd+i;
            }
            else{
                totaleven=totaleven+i;
            }
          
        }
        
        System.out.print("sum of all even numbers:"+totaleven+"\n");
        System.out.print("sum of all odd numbers:"+totalodd);
    }
}

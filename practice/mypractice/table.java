import java.util.*;
class table{
    public static void main(String args[]){
        int n;
        Scanner obj = new Scanner(System.in);
        System.out.print("enter the number to make its multiplication table:");
        n=obj.nextInt();
        
        for(int i=1;i<=10;i++){
            System.out.print(+n+" multiply by "+i+" = "+(n*i)+"\n");
        }
        obj.close();    
    }
}

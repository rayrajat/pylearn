import java.util.*;
class marks{
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String args[]){
        int total=0;int n;int marks;int avg;
        Scanner obj = new Scanner(System.in);
        System.out.print("enter number of subjects:");
        n=obj.nextInt();
        for(int i=1;i<=n;i++){
            System.out.print("enter marks for subject"+i+":");
            marks=obj.nextInt();
            
            total=total+marks;
        }
        
        avg=total/n;
        
        System.out.print("total marks for"+n+"subjects is "+total+"\n");
        System.out.print("average marks for"+n+"subjects is "+avg);
        
        obj.close();
    
    }
}

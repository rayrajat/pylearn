import java.util.*;
class ascii{
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String args[]){
        char ch;
        Scanner obj = new Scanner(System.in);
        System.out.print("enter character:");
        ch = obj.next().charAt(0);
        
        int a = ch;
        
        System.out.print("ascii value of " +ch+ " is  " +a);
        obj.close();
    }
}

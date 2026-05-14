import java.util.*;
class charprint{
    public static void main(String args[]){
        char ch;
        @SuppressWarnings("resource")
        Scanner obj=new Scanner(System.in);
        System.out.print("enter string:");
        ch=obj.next().charAt(0);
        System.out.print("entered character:"+ch);
    }
}

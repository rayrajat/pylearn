import java.util.*;
class vowel{
    public static void main(String args[]){
        char ch;
        Scanner obj = new Scanner(System.in);
        System.out.print("enter character:");
        ch=obj.next().charAt(0);
    
        
        char lowch=Character.toLowerCase(ch);
        
        if(lowch=='a'||lowch=='e'||lowch=='i'||lowch=='o'||ch=='u'){
            System.out.print("vowel");
        }
        else{
            System.out.print("Consonant");
        }
    }
}

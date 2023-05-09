import java.util.Scanner;

public class BOJ2744 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String result = "";
        for(int i=0; i<s.length() ;i++){
            char c = s.charAt(i);
            result += Character.isLowerCase(c) ? Character.toUpperCase(c) : Character.toLowerCase(c);
        }
        System.out.println(result);
        sc.close();
    }
}

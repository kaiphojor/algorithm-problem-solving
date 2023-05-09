import java.util.Scanner;

public class BOJ2609 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int gcdValue = gcd(A,B);
        int lcmValue = A * B / gcdValue;
        System.out.println(gcdValue);
        System.out.println(lcmValue);
        sc.close();
    }
    public static int gcd(int a,int b){
        if(a > b){
            int c = a;
            a = b;
            b = c;
        }
        while (a != 0){
            int mod = b % a;
            b = a;
            a = mod;
        }
        return b;
    }
}

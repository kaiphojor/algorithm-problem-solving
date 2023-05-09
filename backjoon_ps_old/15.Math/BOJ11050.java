import java.util.Scanner;

public class BOJ11050 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int result = 1;
        for(int i=1; i<=N; i++){
            result *= i;
        }
        for(int i=1; i<=K; i++){
            result /= i;
        }
        for(int i=1; i<=N-K; i++){
            result /= i;
        }
        System.out.println(result);
        sc.close();
    }
}

import java.util.Scanner;

public class BOJ1929 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();
        int[] primeNumbers = new int[N+1];
        primeNumbers[1] = -1;
        for(int i=2; i <= N ; i++){
            if(primeNumbers[i] != -1){
                int j = 2;
                int mult;
                while ((mult = i * j++) <= N){
                    primeNumbers[mult] = -1;
                }
            }
        }
        for(int i=M; i<=N ; i++){
            if(primeNumbers[i] != -1){
                System.out.println(i);
            }
        }
        sc.close();
    }
}

import java.util.Scanner;

public class BOJ1676 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int twoCount = 0;
        int fiveCount = 0;
        for(int i=1; i<=N ;i++){
            int n = i;
            while(n % 2 == 0){
                n /=  2;
                twoCount++;
            }
            while(n% 5 == 0){
                n /= 5;
                fiveCount++;
            }
        }
        int result = Math.min(twoCount,fiveCount);
        System.out.println(result);
        sc.close();
    }
}

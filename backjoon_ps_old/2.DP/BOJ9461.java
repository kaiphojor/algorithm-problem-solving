import java.util.Scanner;
/*
 * 1 1 1 2 2 3 4 5 7 9
 * a(N) = a(N-2) + a(N-3)
 */
public class BOJ9461 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int t=0; t<T ; t++){
            int N = sc.nextInt();
            long[] triangleSequence = new long[N+1];
            triangleSequence[1] = 1;
            if(N >= 2){
                triangleSequence[2] = 1;
            }
            if(N >= 3){
                triangleSequence[3] = 1;                
                for(int i=4; i<=N; i++){
                    triangleSequence[i] = triangleSequence[i-2] + triangleSequence[i-3];
                }
            }
            System.out.println(triangleSequence[N]);
        }
        sc.close();
    }
}

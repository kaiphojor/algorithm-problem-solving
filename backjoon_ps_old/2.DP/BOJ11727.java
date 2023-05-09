import java.util.Scanner;

/*
 * 1 - 1
 * 2 - 3
 * 3 - 5  =1 1= 111 ㅁ1 1ㅁ 
 * 4 - 11   1111 11= 11ㅁ =11 == =ㅁ ㅁ11 ㅁ= ㅁㅁ 1ㅁ1 1=1
 * a(N) = a(N-1) + 2 * a(N-1)
 */
public class BOJ11727 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] numberOfCases = new int[n+1];
        numberOfCases[1] = 1;
        if( n >= 2){
            numberOfCases[2] = 3;
            for(int i=3; i <= n ; i++){
                numberOfCases[i] = (numberOfCases[i-1] + 2 * numberOfCases[i-2]) % 10007;
            }
        }
        System.out.println(numberOfCases[n]);
        sc.close();
    }
}

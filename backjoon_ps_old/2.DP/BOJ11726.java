import java.util.Scanner;

public class BOJ11726 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] numberOfCases = new int[n+1];
        numberOfCases[1] = 1;
        if(n >= 2){
            numberOfCases[2] = 2;
            for(int i=3; i<=n; i++){
                numberOfCases[i] = (numberOfCases[i-1] + numberOfCases[i-2]) % 10007;
            }
        }
        System.out.println(numberOfCases[n]);        
        sc.close();
    }
}
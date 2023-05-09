import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ11047 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            int[] coinValues = new int[N];
            for( int i=N-1; i>=0 ; i--){
                coinValues[i] = Integer.parseInt(br.readLine());
            }
            int n = 0;
            int coinCount = 0 ;
            while(K > 0 && n < N){
                if(coinValues[n] <= K){
                    int currentCoinCount = K / coinValues[n];
                    coinCount += currentCoinCount;
                    K -= currentCoinCount * coinValues[n];
                }
                n++;
            }
            bw.write(coinCount + "\n");

            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

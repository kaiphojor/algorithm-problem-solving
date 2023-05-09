import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ2775 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int T = Integer.parseInt(br.readLine());
            for(int t=0; t<T; t++){
                int k = Integer.parseInt(br.readLine());
                int n = Integer.parseInt(br.readLine());
                int[][] arr = new int[k+1][n+1];
                for(int i=1; i<=n ; i++ ){
                    arr[0][i] = i;
                }
                for(int i=1; i<=k; i++){
                    for(int j=1; j<=n; j++){
                        for(int l=1; l<=j; l++){
                            arr[i][j] += arr[i-1][l];
                        }
                    }
                }
                bw.write(arr[k][n]+"\n");
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

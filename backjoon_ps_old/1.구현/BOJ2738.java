import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.concurrent.atomic.AtomicInteger;

public class BOJ2738 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        try {
            String[] nmString = br.readLine().split(" ");
            int N = Integer.parseInt(nmString[0]);
            int M = Integer.parseInt(nmString[1]);
            int[][] arr = new int[N][M];
            for(int a=0; a<2; a++){
                for(int i=0; i< N; i++){
                    final int iFinal = i;
                    String[] rowString = br.readLine().split(" ");
                    AtomicInteger indexHolder = new AtomicInteger();
                    Arrays
                    .asList(rowString)
                    .stream()
                    .map(Integer::parseInt)
                    .forEach((n) -> {
                        int j = indexHolder.getAndIncrement();
                        arr[iFinal][j] += n;
                    });
                }
            }
            for(int i=0; i < N; i++){
                for(int j=0; j<M; j++){
                    bw.write(arr[i][j] + " ");
                }
                bw.write("\n");
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

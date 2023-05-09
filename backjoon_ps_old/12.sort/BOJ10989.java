import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ10989 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[10001];
            for(int i=0; i<N ; i++){
                arr[Integer.parseInt(br.readLine())] += 1;
            }
            for(int i = 1; i<= 10000; i++){
                for( int j = 1 ; j <= arr[i]; j++){
                    bw.write(i+"\n");
                }
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

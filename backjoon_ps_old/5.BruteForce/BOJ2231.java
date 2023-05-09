import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class BOJ2231 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int N = Integer.parseInt(br.readLine());
            int decompositionSum = 0;
            for(int i=1; i<N; i++){
                
                int partialSum = Arrays
                .stream(String.valueOf(i).split(""))
                .map(Integer::parseInt)
                .reduce(0,(a,b)->a+b);
                int M = i + partialSum;
                
                if(N == M){
                    decompositionSum = i;
                    break;
                }
            }
            bw.write(decompositionSum+"\n");

            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ1541 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            StringTokenizer st = new StringTokenizer(br.readLine(),"-");
            int total = 0;
            
            for(int i=0; st.hasMoreTokens() ; i++){
                StringTokenizer partialTokenizer = new StringTokenizer(st.nextToken(),"+");
                int partialSum = 0;
                
                while(partialTokenizer.hasMoreTokens()){
                    partialSum += Integer.parseInt(partialTokenizer.nextToken());
                }
                
                total = i == 0 ? total + partialSum : total - partialSum;
            }
            
            bw.write(total + "\n");
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }           
    }
}

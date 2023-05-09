import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ15552 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int T = Integer.parseInt(br.readLine());
            for(int i=0; i<T; i++){
                String[] splitted = br.readLine().split(" ");
                int abSum = Integer.parseInt( splitted[0]) + Integer.parseInt( splitted[1]); 
                bw.write(abSum + "\n");
            }
            bw.flush();
            br.close();
            bw.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }    
}

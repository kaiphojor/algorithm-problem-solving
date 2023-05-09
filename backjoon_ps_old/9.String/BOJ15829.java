import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ15829 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int L = Integer.parseInt(br.readLine());
            String[] strings = br.readLine().trim().split("");
            long total = 0;
            int mod = 1234567891;
            for(int i=0; i<L; i++){
                long value = strings[i].charAt(0) - 'a' + 1;
                long powered = value;
                for(int j=0; j<i; j++){
                    powered *= 31;
                    if(powered > mod){
                        powered %= mod;
                    }
                }
                total += powered;
                total %= mod;
            }
            long resultHashValue = total % mod;
            bw.write(resultHashValue + "\n");
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

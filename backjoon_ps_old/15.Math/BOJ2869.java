import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ2869 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            String[] abvString = br.readLine().split(" ");
            
            int A = Integer.parseInt(abvString[0]);
            int B = Integer.parseInt(abvString[1]);
            int V = Integer.parseInt(abvString[2]);
            int movePerDay = A - B;
            int length = V - A;
            int days = length / movePerDay + 1;
            int remain = length % movePerDay;
            if( remain > 0 ){
                days++;
            }
            bw.write(days+"\n");
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

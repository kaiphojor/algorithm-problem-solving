import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ10951 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            for(String line = br.readLine(); line != null ; line=br.readLine()){
                StringTokenizer st = new StringTokenizer(line," ");
                int A = Integer.parseInt(st.nextToken());
                int B = Integer.parseInt(st.nextToken());
                System.out.println(A + B);
            }
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
    
}

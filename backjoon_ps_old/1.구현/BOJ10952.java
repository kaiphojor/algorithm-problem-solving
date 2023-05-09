import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ10952 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            while(true){
                StringTokenizer st = new StringTokenizer(br.readLine()," ");
                if( st.countTokens() == 2){
                    int A = Integer.parseInt(st.nextToken());
                    int B = Integer.parseInt(st.nextToken());
                    if( A == 0 && B == 0){
                        break;
                    }
                    System.out.println(A + B);
                }
            }
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
    
}

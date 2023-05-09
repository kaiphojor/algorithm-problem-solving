import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ1330 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            if( A < B ){
                System.out.println("<");
            }else if ( A > B ){
                System.out.println(">");
            }else{
                System.out.println("==");
            }
            
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }finally{
        }
    }
    
}

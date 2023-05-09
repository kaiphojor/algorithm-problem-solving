import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
/*
 * 10i + x = 
 * 12j + y 
 */
public class BOJ6064 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            int T = Integer.parseInt(br.readLine());
            for(int t=0; t<T; t++){
                StringTokenizer st = new StringTokenizer(br.readLine()," ");
                int M = Integer.parseInt(st.nextToken());
                int N = Integer.parseInt(st.nextToken());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                if( x == M){
                    x = 0;
                }
                if( y == N){
                    y = 0;
                }
                int lcm = getLcm(M,N);
                boolean isValid = false;
                int number = x;
                
                for( ; number <= lcm ; number += M){
                    if(number % N == y){
                        isValid = true;
                        break;
                    }
                }
                if(isValid){
                    if(number == 0){
                        number = lcm;
                    }
                    bw.write(number + "\n");
                }else{
                    bw.write(-1 + "\n");
                }
                
            }
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static int getLcm(int m, int n) {
        int multiple = m * n;
        if(m < n){
            int box = m;
            m = n;
            n = box;
        }
        while(n != 0){
            int box = m % n;
            m = n;
            n = box;
        }
        return multiple / m;
    }

}

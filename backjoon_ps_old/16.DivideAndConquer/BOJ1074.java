import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

/*
 * 0 11
 * 1 12
 * 2 21
 * 3 22
 * 4 13
 * 5 14
 * 6 23
 * 7 24
 * 8 31
 * 9 32
 * 1041
 * 1142
 * 4분할 범위 확인 2 시작이면 1 적게 
 * 2의 1 승 2를 기준 > 사분면 나누기
 * <= <= 1사분면 <= > 2사분면 > <= 3사분면 > > 4사분면
 * 0 , 1 * 2^1 * 2^1  
 * 1사분면 안짜름 2 열 2^1만큼 - 3 행 2^1만큼- 4 행열 2^1만큼
 * 2의 0승 1을 기준 
 * 1 기준
 * 1사분면
 * 0 1 * 2^0 1 * 2^0 
 * 
 * 
 */
public class BOJ1074 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            int N = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            r++;
            c++;
            int order = 0;
            while(N > 0){
                int threshold = (int)Math.pow(2, N-1);
                if(r > threshold){
                    order += 2 * threshold * threshold;
                    r -= threshold;
                }
                if(c > threshold){
                    order += threshold * threshold;
                    c -= threshold;
                }                
                N--;
            }
            bw.write(order + "\n");
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

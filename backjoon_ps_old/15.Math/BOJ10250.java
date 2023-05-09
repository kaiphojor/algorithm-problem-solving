import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ10250 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int T = Integer.parseInt(br.readLine());
            for(int t=0; t<T ; t++){
                StringTokenizer st = new StringTokenizer(br.readLine()," ");
                int H = Integer.parseInt(st.nextToken());
                int W = Integer.parseInt(st.nextToken());
                int N = Integer.parseInt(st.nextToken());
                int div = N / H; 
                int mod = N % H;
                int floor = mod == 0 ? H : mod;
                int order = mod == 0 ? div : div + 1;
                int roomNumber = floor * 100 + order;
                bw.write(roomNumber + "\n");
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

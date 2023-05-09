import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ2675 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int T = Integer.parseInt(br.readLine());
            for(int t=0 ; t<T ; t++){
                StringTokenizer st = new StringTokenizer(br.readLine()," ");
                int iterationCount = Integer.parseInt(st.nextToken());
                String s = st.nextToken();
                for(int i=0 ; i< s.length() ;i++){
                    String chr = s.charAt(i)+"";
                    for(int j=0; j < iterationCount ; j++){
                        bw.write(chr);
                    }
                }
                bw.write("\n");
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

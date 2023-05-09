import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ11866 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            List<String> queue = new ArrayList<>();
            List<String> sequence = new ArrayList<>();
            for(int i=1; i<= N ; i++){
                queue.add(i+"");
            }
            int i = 0;
            while(!queue.isEmpty()){
                i+=K-1;
                while (queue.size() <= i){
                    i = i - queue.size();
                }
                sequence.add(queue.remove(i));
            }
            StringBuilder sb = new StringBuilder();
            sb.append("<");
            sb.append(String.join(", ",sequence));
            sb.append(">");
            bw.write(sb.toString());
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

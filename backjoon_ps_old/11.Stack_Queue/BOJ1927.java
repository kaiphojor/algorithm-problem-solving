import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;

public class BOJ1927 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            int N = Integer.parseInt(br.readLine());
            PriorityQueue<Integer> queue = new PriorityQueue<>();
            for(int i=0; i<N ; i++){
                int n = Integer.parseInt(br.readLine());
                if(n == 0){
                    if(queue.size() == 0){
                        bw.write(0 + "\n");
                    }else{
                        bw.write(queue.poll()+"\n");
                    }
                }else{
                    queue.add(n);
                }
            }

            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

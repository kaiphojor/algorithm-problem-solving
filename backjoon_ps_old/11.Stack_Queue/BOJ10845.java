import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ10845 {

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] queue = new int[10000];
        int front = -1;
        int rear = -1;
        try {
            int N = Integer.parseInt(br.readLine());
            for(int i=0; i<N ; i++){
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                String command = st.nextToken();
                if("push".equals(command)){
                    int item = Integer.parseInt(st.nextToken());
                    queue[++rear] = item;
                }else if("pop".equals(command)){
                    if(front == rear){
                        bw.write(-1+"\n");
                    }else{
                        int popped = queue[++front];
                        bw.write(popped+"\n");
                    }
                }else if("front".equals(command)){
                    if(front == rear){
                        bw.write(-1+"\n");
                    }else{
                        bw.write(queue[front+1]+"\n");
                    }
                }else if("back".equals(command)){
                    if(front == rear){
                        bw.write(-1+"\n");
                    }else{
                        bw.write(queue[rear]+"\n");
                    }
                }else if("size".equals(command)){
                    bw.write(rear-front+"\n");
                }else if("empty".equals(command)){
                    bw.write((front == rear ? 1 : 0) + "\n");
                }
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ10866 {

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        List<Integer> deque = new LinkedList<Integer>();
        int size = 0;
        try {
            int N = Integer.parseInt(br.readLine());
            for(int i=0; i<N ; i++){
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                String command = st.nextToken();
                if("push_front".equals(command)){
                    int item = Integer.parseInt(st.nextToken());
                    deque.add(item);
                    size++;
                }else if("push_back".equals(command)){
                    int item = Integer.parseInt(st.nextToken());
                    deque.add(0,item);
                    size++;
                }else if("pop_front".equals(command)){
                    if(size == 0){
                        bw.write(-1+"\n");
                    }else{
                        int item = deque.remove(--size);
                        bw.write(item+"\n");
                    }
                }else if("pop_back".equals(command)){
                    if(size == 0){
                        bw.write(-1+"\n");
                    }else{
                        int item = deque.remove(0);
                        bw.write(item+"\n");
                        size--;
                    }
                }else if("front".equals(command)){
                    if(size==0){
                        bw.write(-1+"\n");
                    }else{
                        bw.write(deque.get(size-1)+"\n");
                    }
                }else if("back".equals(command)){
                    if(size==0){
                        bw.write(-1+"\n");
                    }else{
                        bw.write(deque.get(0)+"\n");
                    }
                }else if("size".equals(command)){
                    bw.write(size+"\n");
                }else if("empty".equals(command)){
                    bw.write((size==0 ? 1 : 0) + "\n");
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

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ10828 {

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] stack = new int[10000];
        int top = -1;
        try {
            int N = Integer.parseInt(br.readLine());
            for(int i=0; i<N ; i++){
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                String command = st.nextToken();
                if("push".equals(command)){
                    int item = Integer.parseInt(st.nextToken());
                    stack[++top] = item;
                }else if("pop".equals(command)){
                    if(top == -1){
                        bw.write(-1+"\n");
                    }else{
                        int popped = stack[top--];
                        bw.write(popped+"\n");
                    }
                }else if("top".equals(command)){
                    if(top == -1){
                        bw.write(-1+"\n");
                    }else{
                        bw.write(stack[top]+"\n");
                    }
                }else if("size".equals(command)){
                    bw.write(top+1+"\n");
                }else if("empty".equals(command)){
                    bw.write((top == -1 ? 1 : 0) + "\n");
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

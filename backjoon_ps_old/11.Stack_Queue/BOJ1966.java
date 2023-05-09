import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ1966 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int T = Integer.parseInt(br.readLine());
            for(int t=0 ; t<T ; t++){
                String[] nm = br.readLine().split(" ");
                int N = Integer.parseInt(nm[0]);
                int M = Integer.parseInt(nm[1]);
                if( N != 1){
                    StringTokenizer st = new StringTokenizer(br.readLine()," ");
                    Queue<List<Integer>> queue = new LinkedList<>(); 
                    List<Integer> orderResult = new ArrayList<>();
                    int i=0;
                    while(st.hasMoreTokens()){
                        List<Integer> li = new ArrayList<>();
                        li.add(i++);
                        li.add(Integer.parseInt(st.nextToken()));
                        queue.add(li);
                    }
                    List<Integer> curList;
                    while((curList = queue.peek()) != null){
                        int maxImportance = 0;
                        for(List<Integer> li : queue){
                            maxImportance = Math.max(maxImportance,li.get(1));
                        }
                        if(curList.get(1) == maxImportance){
                            orderResult.add(queue.poll().get(0));
                        }else{
                            queue.add(queue.poll());
                        }
                    }
                    bw.write(orderResult.indexOf(M)+1 + "\n");
                }else{
                    br.readLine();
                    bw.write(1+"\n");
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

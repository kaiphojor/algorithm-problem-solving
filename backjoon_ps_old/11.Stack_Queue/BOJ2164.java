import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;

public class BOJ2164 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int N = Integer.parseInt(br.readLine());
            LinkedList<Integer> list = new LinkedList<>();
            for(int i=1; i<=N; i++){
                list.add(i);
                
            }
            while(list.size()>1){
                list.removeFirst();
                if(list.size() == 1){break;}
                list.add(list.removeFirst());
            }
            bw.write(list.get(0)+"\n");
            
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

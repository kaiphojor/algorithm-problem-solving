import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class BOJ10773 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int K = Integer.parseInt(br.readLine());
            List<Integer> list = new ArrayList<>();
            for(int i=0; i<K ; i++){
                int item = Integer.parseInt(br.readLine());
                if(item == 0){
                    list.remove(list.size()-1);
                }else{
                    list.add(item);
                }
            }
            int total = list.stream().reduce(0,(a,b)-> a+b).intValue();
            bw.write(total + "\n");
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

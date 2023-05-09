import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BOJ2562 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            List<Integer> arr = new ArrayList<>();
            String line;
            while((line = br.readLine()) != null){
                if(line.isEmpty()){ break; }
                int num = Integer.parseInt(line);
                arr.add(num);
            }
            int maxValue = Collections.max(arr);
            bw.write(maxValue + "\n");
            bw.write(arr.indexOf(maxValue) + 1+"\n");
            
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

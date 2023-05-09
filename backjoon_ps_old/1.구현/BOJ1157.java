import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class BOJ1157 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            Map<String,Integer> frequencyMap = new HashMap<String,Integer>();
            Arrays
            .asList(br.readLine().split(""))
            .stream()
            .forEach((k)-> {
                String key = k.toUpperCase();
                frequencyMap.put(key,frequencyMap.getOrDefault(key, 0)+1);
            });
            Collection<Integer> values = frequencyMap.values();
            int maxValue = values.stream().mapToInt(x->x).max().orElse(0);
            long maxCount = values.stream().filter(x->x==maxValue).count();
            if(maxCount >= 2 ){
                bw.write("?\n");
            }else{
                for(Map.Entry<String,Integer> entry :frequencyMap.entrySet()){
                    if(entry.getValue() == maxValue){
                        bw.write(entry.getKey()+"\n");
                        break;
                    }
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

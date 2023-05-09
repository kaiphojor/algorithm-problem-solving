import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ9375 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            int T = Integer.parseInt(br.readLine());
            StringTokenizer st;
            for(int t=0; t<T; t++){
                Map<String,Integer> clothesMap = new HashMap<String,Integer>();
                int N = Integer.parseInt(br.readLine());
                for(int n=0; n<N; n++){
                    st = new StringTokenizer(br.readLine()," ");
                    st.nextToken();
                    String category = st.nextToken();
                    if(clothesMap.containsKey(category)){
                        clothesMap.put(category,clothesMap.get(category) + 1);
                    }else{
                        clothesMap.put(category,2);
                    }
                }

                int numberOfCases = 1;
                for(String key : clothesMap.keySet()){
                    numberOfCases *= clothesMap.get(key);
                }
                numberOfCases--;

                bw.write(numberOfCases + "\n");
            }
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

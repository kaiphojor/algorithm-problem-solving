import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ1931 {
    public static void main(String[] args) {

        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            int N = Integer.parseInt(br.readLine());
            List<int[]> list = new ArrayList<>();

            for(int i=0; i<N ; i++){
                StringTokenizer st = new StringTokenizer(br.readLine()," ");
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                list.add(new int[]{s, e});
            }

            Collections.sort(list,new Comparator<int[]>(){
                @Override
                public int compare(int[] o1, int[] o2) {
                    int result = o1[1] - o2[1];
                    if(result == 0){
                        result = o1[0] - o2[0];
                    }
                    return result;
                }                
            });
            
            int finishedTime = -1;
            int sessionCount = 0;
            for(int i=0; i< list.size() ; i++){
                int[] item = list.get(i);
                if(finishedTime <= item[0]){
                    finishedTime = item[1];
                    sessionCount++;                    
                }
            }

            bw.write(sessionCount + "\n");
            bw.flush();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ18111 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int[] heights = new int[257];
            for(int i=0; i < N ; i++){
                st = new StringTokenizer(br.readLine()," ");
                for(int j=0; j<M; j++){
                    heights[Integer.parseInt(st.nextToken())] += 1;
                }
            }
            int boxLeft = B;
            int time = 0;
            List<int[]> list = new ArrayList<int[]>();
            for(int k = 0; k <= 256 ; k++){
                boxLeft = B;
                time = 0;
                for(int i = k + 1 ; i<=256; i++){
                    if(heights[i] > 0){
                        int flattenCount = (i-k) * heights[i];
                        boxLeft += flattenCount;
                        time += flattenCount * 2;
                    }
                }
                for(int i=0; i < k; i++){
                    if(heights[i] > 0){
                        int fillCount = (k-i) * heights[i];
                        boxLeft -= fillCount;
                        time += fillCount;
                    }
                }
                if(boxLeft >= 0 ){
                    list.add(new int[]{time, k});
                }
            }
            list.sort(new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    int result = o1[0] - o2[0];
                    if(result == 0){
                        result = o2[1] - o1[1];
                    }
                    return result;
                }                
            });
            int[] item = list.get(0);
            bw.write(item[0] + " " + item[1] + "\n");
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

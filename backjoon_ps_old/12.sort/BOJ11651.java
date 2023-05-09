import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ11651 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int N = Integer.parseInt(br.readLine());
            List<int[]> list = new ArrayList<>();
            for(int i=0; i<N ; i++){
                StringTokenizer st = new StringTokenizer(br.readLine()," ");
                int[] item = new int[2];
                item[0] = Integer.parseInt(st.nextToken());
                item[1] = Integer.parseInt(st.nextToken());
                list.add(item);
            }
            list.sort(new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    int result = o1[1] - o2[1];
                    if(result == 0){
                        result = o1[0] - o2[0];
                    }
                    return result;
                }                
            });
            for(int[] item : list){
                bw.write(item[0] + " " + item[1] + "\n");
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

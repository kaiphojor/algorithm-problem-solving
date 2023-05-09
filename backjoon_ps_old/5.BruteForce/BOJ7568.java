import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ7568 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int N = Integer.parseInt(br.readLine());
            List<int[]> list = new ArrayList<>();
            for(int i=0; i<N; i++){
                StringTokenizer st = new StringTokenizer(br.readLine()," ");
                int[] personInfo = new int[3];
                personInfo[0] = i;
                personInfo[1] = Integer.parseInt(st.nextToken());
                personInfo[2] = Integer.parseInt(st.nextToken());
                list.add(personInfo);                
            }
            Collections.sort(list,new Comparator<int[]>(){
                @Override
                public int compare(int[] o1, int[] o2) {
                    int result = o1[1] - o2[1];
                    if(result == 0){
                        result = o1[2] - o2[2];
                    }
                    return -result;
                }

            });
            int[] orders = new int[N];
            for( int i=0; i < N ; i++){
                // int rank = 1;
                int[] item = list.get(i);
                // System.out.println(item[0] +" " +item[1] +" " +item[2] +" ");
                if(i==0){
                    orders[item[0]] = 1;
                }else{
                    int order = 1;
                    for(int j=0; j<i; j++){
                        int[] previous = list.get(j);
                        if(previous[2] > item[2] && previous[1] > item[1]){
                            order++;                        
                        }
                    }
                    orders[item[0]] = order;
                }
            }
            for (int i : orders) {
                System.out.print(i + " ");
            }
            
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BOJ2798 {
    public static int closestCombination(int[] arr, boolean[] visited, int start, int n, int r, int limit){
        if(r == 0){
            int combinationSum = 0;
            for(int i=0; i<n; i++){
                if(visited[i]){
                    combinationSum += arr[i];
                }
            }

            return combinationSum <= limit ? combinationSum : 0;
        }else{
            List<Integer> sums = new ArrayList<>();
            sums.add(0);
            for(int i=start; i<n ; i++){
                visited[i] = true;
                int currentSum = closestCombination(arr,visited,i+1,n, r-1, limit);
                sums.add(currentSum);
                visited[i] = false;
            }
            return Collections.max(sums);
        }
    }
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            String[] nmString = br.readLine().split(" ");
            int N = Integer.parseInt(nmString[0]);
            int M = Integer.parseInt(nmString[1]);
            String[] inputString = br.readLine().split(" ");
            int[] arr = new int[N];
            boolean[] visited = new boolean[N];
            
            // List<Integer> list = new ArrayList<>();
            for(int i=0; i<N; i++){
                arr[i] = Integer.parseInt(inputString[i]);
                // list.add(Integer.parseInt(inputString[i]));
            }
            // list = list.stream().sorted().collect(Collectors.toList());
            int blackjackSum = closestCombination(arr, visited, 0, N, 3, M);
            bw.write(blackjackSum+"\n");
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

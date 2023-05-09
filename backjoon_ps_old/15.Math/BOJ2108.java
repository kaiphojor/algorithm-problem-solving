import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BOJ2108 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int N = Integer.parseInt(br.readLine());

            List<Integer> maxFrequencies = new ArrayList<>();
            int[] arr = new int[8001];
            int sumValue = 0;
            for(int i=0; i<N; i++){
                int n = Integer.parseInt(br.readLine());
                arr[n+4000] += 1;
                sumValue += n;
            }
            
            int minValue = 4000, maxValue = -4000;
            for(int i=0;i<=8000; i++){
                if(arr[i] != 0){
                    minValue = i-4000;
                    break;
                }
            }
            for(int i=8000; i>=0; i--){
                if(arr[i] != 0){
                    maxValue = i-4000;
                    break;
                }
            }
            int half = N / 2  + 1;
            int mode = 4001;
            int order = 0;
            for(int i=minValue+4000; i<=maxValue+4000; i++){
                if(arr[i] != 0){
                    order += arr[i];
                    if(order >= half){
                        mode = i-4000;
                        break;
                    }
                }
            }

            int maxFrequency = Arrays.stream(arr).max().getAsInt();
            for(int i=0; i<= 8000; i++){
                if(arr[i] == maxFrequency){
                    maxFrequencies.add(i-4000);
                }
            }
            int maxFrequencyNumber = -4001;
            if(maxFrequencies.size() > 1){
                maxFrequencyNumber = maxFrequencies.get(1);
            }else{
                maxFrequencyNumber = maxFrequencies.get(0);
            }
            
            int meanValue = Math.round(sumValue/(float)N);
            bw.write(meanValue+"\n");
            bw.write(mode+"\n");
            bw.write(maxFrequencyNumber+"\n");
            int numberRange = maxValue - minValue;
            bw.write(numberRange+"\n");
            
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

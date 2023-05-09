import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class BOJ1978 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int N = Integer.parseInt(br.readLine());
            
            List<Integer> numbers = Arrays
            .asList(br.readLine().split(" "))
            .stream()
            .map(Integer::parseInt)
            .sorted()
            .collect(Collectors.toList());
            
            int maxValue = Collections.max(numbers);
            int[] isPrimeNumber = new int[maxValue+1];
            isPrimeNumber[1] = -1;
            for(int i=2; i<= maxValue ; i++){
                if( isPrimeNumber[i] != -1 ){
                    int j = 1;
                    int mult;
                    while((mult = i * ++j) <= maxValue){
                        isPrimeNumber[mult] = -1;
                    }
                }
            }
            long primeNumberCount = numbers.stream().filter(x->isPrimeNumber[x] != -1).count();
            bw.write(primeNumberCount + "\n");
            
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

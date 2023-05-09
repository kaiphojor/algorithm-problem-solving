import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Optional;

public class BOJ10950 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            int testCase = Integer.parseInt(br.readLine());
            for(int i = 0 ; i < testCase ; i++){
                Optional<Integer> summation = Arrays
                .asList(br.readLine().split(" "))
                .stream()
                .map(Integer::parseInt)
                .reduce(Integer::sum);
                summation.ifPresent(System.out::println);             
            }
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

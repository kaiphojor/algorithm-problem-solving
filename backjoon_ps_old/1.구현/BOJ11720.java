import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Collectors;

// Main으로 제출할것
public class BOJ11720{
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        try {
            Integer.parseInt(br.readLine());
            String[] inputArr = br.readLine().strip().split("");
            int result = Arrays.asList(inputArr).stream().collect(Collectors.summingInt(Integer::parseInt));
            System.out.println(result);
            
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        
    }
}
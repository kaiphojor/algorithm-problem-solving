import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.OptionalDouble;
import java.util.StringTokenizer;

public class BOJ1546 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            int N = Integer.parseInt(br.readLine());
            List<Integer> arr = new ArrayList<>();
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            while(st.hasMoreTokens()){
                arr.add(Integer.parseInt(st.nextToken()));
            }
            int maxValue = Collections.max(arr);
            OptionalDouble averageOptional = arr
                                                .stream()
                                                .mapToDouble((t) -> t * 100.0 / maxValue )
                                                .average();
            averageOptional.ifPresent(System.out::println);

            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

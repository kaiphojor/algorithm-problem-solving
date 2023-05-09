import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Optional;
// import java.util.StringTokenizer;

public class BOJ2420 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            // StringTokenizer st = new StringTokenizer(br.readLine()," ");
            // long N = Long.parseLong(st.nextToken());
            // long M = Long.parseLong(st.nextToken());
            // long difference = N - M > 0 ? N-M : M-N;
            // System.out.println(difference);
            Optional<Long> difference = Arrays
                                        .asList(br.readLine().split(" "))
                                        .stream()
                                        .map(Long::parseLong)
                                        .reduce((a,b)-> a>b? a-b: b-a);

            difference.ifPresent(System.out::println);

            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

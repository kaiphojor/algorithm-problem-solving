import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.stream.Collectors;

public class BOJ10807 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        try {
            int N = Integer.parseInt(br.readLine());
            String[] inputNumberStrings = br.readLine().split(" ");
            int v = Integer.parseInt(br.readLine());
            int vCount = Arrays
                            .asList(inputNumberStrings)
                            .stream()
                            .map(Integer::parseInt)
                            .filter((n)-> n == v)
                            .collect(Collectors.toList())
                            .size();
            bw.write(String.valueOf(vCount));
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

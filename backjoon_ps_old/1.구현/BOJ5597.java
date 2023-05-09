import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class BOJ5597 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        try {
            List<Integer> arr = new ArrayList<>();
            for(int i=0; i< 28; i++){
                arr.add(Integer.parseInt(br.readLine()));
            }
            IntStream
            .rangeClosed(1,30)
            .filter((n)-> !arr.contains(n))
            .forEachOrdered((n)->{
                try {
                    bw.write(n+"\n");
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            });
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }

    }
}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class BOJ1152 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            String inputString = br.readLine().trim();
            int wordCount = inputString.length() == 0 ? 0 : Arrays.asList(inputString.split(" ")).size();
            // 개행 안넣으면 문자로 들어간다
            bw.write(wordCount+"\n");
            
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}
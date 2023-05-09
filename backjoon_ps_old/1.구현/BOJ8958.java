import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ8958 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int T = Integer.parseInt(br.readLine());
            for( int t=0; t<T ; t++){
                String oxResult = br.readLine();
                int combo = 0;
                int totalScore = 0;
                for(int i=0; i<oxResult.length() ; i++){
                    String result = oxResult.charAt(i) + "";
                    if("O".equals(result)){
                        combo += 1;
                        totalScore += combo;
                    }else{
                        combo = 0;
                    }
                }
                bw.write(totalScore + "\n");
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

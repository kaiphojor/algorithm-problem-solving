import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ11723 {
    public static void main(String[] args) {

        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {

            int M = Integer.parseInt(br.readLine());
            int[] S = new int[21];
            
            for(int i=0; i<M; i++){
                StringTokenizer st = new StringTokenizer(br.readLine()," ");
                String command = st.nextToken();
                int x = 0;
                if(st.hasMoreTokens()){
                    x = Integer.parseInt(st.nextToken());
                }

                if("all".equals(command)){
                    S = new int[21];
                    for(int j=1; j<=20;j++){
                        S[j] = 1;
                    }
                }else if("empty".equals(command)){
                    S = new int[21];
                }else if("toggle".equals(command)){
                    S[x] ^= 1;
                }else if("check".equals(command)){
                    bw.write(S[x]+"\n");
                }else if("remove".equals(command)){
                    S[x] = 0;
                }else if("add".equals(command)){
                    S[x] = 1;
                }
            }
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }
}

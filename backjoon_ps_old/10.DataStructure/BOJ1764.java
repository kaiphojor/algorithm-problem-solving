import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.Set;
import java.util.SortedSet;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class BOJ1764 {
    public static void main(String[] args) {
        
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            Set<String> neverHeard = new HashSet<>();
            Set<String> neverHeardSeen = new HashSet<>();

            for(int i=1; i<=N; i++){
                neverHeard.add(br.readLine().trim());
            }
            for(int i=1; i<=M; i++){
                String person = br.readLine().trim();
                if(neverHeard.contains(person)){
                    neverHeardSeen.add(person);
                }
            }

            SortedSet<String> sortedResult = new TreeSet<>(neverHeardSeen);
            bw.write(neverHeardSeen.size()+ "\n");
            for(String result : sortedResult){
                bw.write(result + "\n");
            }


            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

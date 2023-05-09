import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ1620 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            String[] pokedexNumber = new String[N+1];
            Map<String,Integer> pokedex = new HashMap<>();
            
            for(int i=1 ; i<=N ; i++){
                String pokemonName = br.readLine().trim();
                pokedexNumber[i] = pokemonName;
                pokedex.put(pokemonName,i);
            }

            for(int i=1; i<=M ; i++){
                String question = br.readLine().trim();
                try {
                    int number = Integer.parseInt(question);
                    bw.write(pokedexNumber[number] + "\n");
                } catch (Exception e) {
                    bw.write(pokedex.get(question)+"\n");
                }
            }

            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

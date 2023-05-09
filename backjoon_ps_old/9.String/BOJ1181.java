import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class BOJ1181 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int N = Integer.parseInt(br.readLine());
            List<String> arr = new ArrayList<>();
            Set<String> wordSet = new HashSet<>();
            for(int i=0; i<N ;i++){
                wordSet.add(br.readLine().trim());
            }
            arr.addAll(wordSet);

            arr.sort(new Comparator<String>() {
                @Override
                public int compare(String o1, String o2) {
                    if ( o1.length() > o2.length() ){
                        return 1;
                    }else if( o1.length() < o2.length()){
                        return -1;
                    }else{
                        if( o1.compareTo(o2) > 0){
                            return 1;
                        }else if(o1.compareTo(o2) < 0){
                            return -1;
                        }else{
                            return 0;
                        }
                    }
                    // TODO Auto-generated method stub                    
                }                
            });
            for(String s : arr){
                bw.write(s + "\n");
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

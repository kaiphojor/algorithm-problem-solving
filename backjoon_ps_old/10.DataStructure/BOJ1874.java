import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/*
 * 1234
 * 12      43
 * 1256
 * 125     436
 * 12578   436
 * 
 */
public class BOJ1874 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int n = Integer.parseInt(br.readLine());

            Stack<Integer> stack = new Stack<>();
            List<Integer> result = new ArrayList<>();
            List<String> operatorList = new ArrayList<>();
            boolean isPossible = true; 
            for(int i=0; i < n ; i++){
                result.add(Integer.parseInt(br.readLine()));
            }
            int number=0;
            for(int r : result){
                while(number < r){
                    number++;
                    stack.push(number);
                    operatorList.add("+");
                    if(number == r){
                        break;
                    }
                }
                int popped = stack.pop();
                if(popped == r){
                    operatorList.add("-");
                }else{
                    isPossible = false;
                    break;
                }
            }
            if(isPossible){
                for(String s : operatorList){
                    bw.write(s+"\n");
                }
            }else{
                bw.write("NO");                
            }

            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

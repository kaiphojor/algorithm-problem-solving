import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class BOJ9012 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            int T = Integer.parseInt(br.readLine());
            for(int t=0; t<T ; t++){
                String s = br.readLine();
                Stack<String> stack = new Stack<String>();
                boolean isVps = true;
                for(int i=0; i<s.length(); i++){
                    String chr = s.charAt(i)+"";
                    if("(".equals(chr)){
                        stack.push(chr);
                    }else if(")".equals(chr)){
                        if(stack.empty()){
                            isVps = false;
                            break;
                        }else{
                            stack.pop();
                        }
                    }                     
                }
                if(!stack.empty()){
                    isVps = false;
                }
                String result = isVps ? "YES": "NO";
                bw.write(result +"\n");
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

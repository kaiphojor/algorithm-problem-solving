import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class BOJ4949 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            while(true){
                String s = br.readLine();
                if(".".equals(s)){
                    break;
                }
                Stack<String> stack = new Stack<String>();
                boolean isBalanced = true;
                for(int i=0; i <s.length(); i++){
                    String chr = s.charAt(i)+"";
                    if("([".contains(chr)){
                        stack.push(chr);
                    }else if("]".equals(chr)){
                        if(stack.empty()){
                            isBalanced = false;
                            break;
                        }else if("[".equals(stack.peek())){
                            stack.pop();
                        }else{
                            isBalanced = false;
                            break;
                        }
                    }else if(")".equals(chr)){
                        if(stack.empty()){
                            isBalanced = false;
                            break;
                        }else if("(".equals(stack.peek())){
                            stack.pop();
                        }else{
                            isBalanced = false;
                            break;
                        }
                    }                    
                }
                if(!stack.empty()){
                    isBalanced = false;
                }
                String result = isBalanced ? "yes" : "no";
                bw.write(result + "\n");
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }

    }
}

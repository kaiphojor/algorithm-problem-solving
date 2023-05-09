import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
/*
 * 3 1  - 3
 * 1 1  - 1
 * 3 2  - 2
 * 4 3   - 2
 * a - b + 1
 */
public class BOJ5525 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            int N = Integer.parseInt(br.readLine());
            int M = Integer.parseInt(br.readLine());
            char[] charArr = br.readLine().trim().toCharArray();
            int totalCaseNumber = 0;
            int start=0,end=0;
            boolean isSequence = false;
            for(int i=0; i<M; i++){
                char newItem = charArr[i];
                if(!isSequence){
                    if(newItem == 'I'){
                        isSequence = true;
                        start = end = i;
                    }
                }else{
                    if(i == M-1){
                        if(newItem == 'I' && newItem != charArr[i-1]){
                            end = i;
                        }

                    }
                    if(newItem == charArr[i-1] || i == M-1){
                        while(charArr[end] == 'O'){
                            end--;
                        }
                        if(start != end){
                            int diff = end - start;
                            if(diff % 2 == 0){
                                int pnCase = diff / 2 - N + 1;
                                totalCaseNumber = pnCase > 0 ? totalCaseNumber + pnCase : totalCaseNumber;
                            }
                        }
                        if(charArr[i] == 'I'){
                            start = end = i;
                        }else{
                            isSequence = false;
                        }
                    }else{
                        end = i;
                    }
                }
            }
            bw.write(totalCaseNumber + "\n");
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

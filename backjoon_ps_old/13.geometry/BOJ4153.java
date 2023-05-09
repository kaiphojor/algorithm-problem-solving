import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ4153 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        try {
            while(true){
                String[] triangleString = br.readLine().split(" ");
                int a = Integer.parseInt(triangleString[0]);
                int b = Integer.parseInt(triangleString[1]);
                int c = Integer.parseInt(triangleString[2]);
                if( a + b + c == 0){
                    break;
                }
                if (a > b){
                    int buffer = a;
                    a = b;
                    b = buffer;
                }
                if (b > c ){
                    int buffer = b;
                    b = c;
                    c = buffer;
                }
                String result = a*a + b * b == c * c ? "right" : "wrong";
                bw.write(result+"\n");
            }
            bw.flush();
            bw.close();
            br.close();
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
}

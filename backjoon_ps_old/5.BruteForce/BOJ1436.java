import java.util.Scanner;

public class BOJ1436 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int nCount = 0;
        int i = 0;
        while(nCount < N){
            String s = String.valueOf(++i);
            if(s.indexOf("666") != -1){
                nCount++;
            }
        }
        System.out.println(i);
        sc.close();
    }
}

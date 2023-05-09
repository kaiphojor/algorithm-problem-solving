import java.util.Scanner;
import java.util.stream.IntStream;

public class BOJ2438 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        IntStream.rangeClosed(1,N).forEach((n)-> {
            for(int i=0 ; i<n;i++){
                System.out.print("*");
            }
            System.out.println();
        });
        sc.close();
    }
}

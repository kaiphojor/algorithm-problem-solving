import java.util.Scanner;
import java.util.stream.IntStream;

public class BOJ10872 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int factorial = IntStream
                        .rangeClosed(1, N)
                        .reduce(1,(a,b)-> a*b);
        System.out.println(factorial);
        sc.close();
    }
}

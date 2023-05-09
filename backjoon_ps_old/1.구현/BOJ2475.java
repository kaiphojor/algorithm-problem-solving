import java.util.Arrays;
import java.util.Scanner;

public class BOJ2475 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total = Arrays
        .asList(sc.nextLine().split(" "))
        .stream()
        .map((c)->{
            int n = Integer.parseInt(c);
            return n * n;
        })
        .reduce(0,Integer::sum);
        System.out.println(total % 10);
        sc.close();
    }
}

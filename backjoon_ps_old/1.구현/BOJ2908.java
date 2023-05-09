import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class BOJ2908 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = getReversedNumber(sc.next());
        int B = getReversedNumber(sc.next());
        System.out.println(Integer.max(A,B));
        sc.close();
    }

    private static int getReversedNumber(String s) {
        List<String> stringList = Arrays.asList(s.split(""));
        Collections.reverse(stringList);
        return Integer.parseInt(String.join("",stringList)); 
    }
}

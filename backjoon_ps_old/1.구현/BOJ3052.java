import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class BOJ3052 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> arr = new ArrayList<>();
        for(int i=0; i< 10 ; i++){
            arr.add(sc.nextInt());
        }
        int result = arr
                    .stream()
                    .map((n) -> n % 42)
                    .collect(Collectors.toSet())
                    .size();
        System.out.println(result);

        sc.close();
    }
}

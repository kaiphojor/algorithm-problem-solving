import java.util.Arrays;
import java.util.Scanner;

public class BOJ2577 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        String ABC = String.valueOf(A * B * C);
        
        for(int i=0; i<=9 ; i++){
            String n = String.valueOf(i);
            long valueCount = Arrays
                                .asList(ABC.split(""))
                                .stream()
                                .filter((e)-> n.equals(e))
                                .count();
                                System.out.println(valueCount);            
        }

        sc.close();
    }
}

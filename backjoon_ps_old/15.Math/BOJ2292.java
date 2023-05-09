import java.util.Scanner;

/*
 * 1 -> 1 1
 * 2 -> 2 12
 * 3 -> 2 13
 * 4 -> 2 14
 * 5 -> 2 15
 * 6 -> 2 16
 * 7 -> 2 17  6
 * 8 -> 3 
 * 19 -> 3    12
 * 37 -> 4    18
 * 
 */
public class BOJ2292 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int step = 1;
        int maxRoomNumber = 1;
        while(N > maxRoomNumber){
            maxRoomNumber += step++ * 6;
        }
        System.out.println(step);

        sc.close();
    }
}

import java.util.Scanner;

public class BOJ1085 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int w = sc.nextInt();
        int h = sc.nextInt();
        int horizontalMinmum = Integer.min(x,w-x);
        int verticalMinimum = Integer.min(y,h-y);
        System.out.println(Integer.min(horizontalMinmum,verticalMinimum));
        sc.close();
    }
}

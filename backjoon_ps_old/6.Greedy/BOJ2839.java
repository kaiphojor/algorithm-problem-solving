import java.util.Scanner;

public class BOJ2839 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int fiveKgCount = N / 5;
        int threeKgCount = 0;
        boolean isMatch = false;
        int remain = N % 5;
        while(fiveKgCount >= 0){
            if(remain % 3 == 0){
                isMatch = true;
                threeKgCount = remain / 3;
                break;
            }
            fiveKgCount--;
            remain += 5;
        }
        int result = isMatch ? fiveKgCount + threeKgCount : -1;
        System.out.println(result);
        sc.close();
    }
}

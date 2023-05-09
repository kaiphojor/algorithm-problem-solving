import java.util.Scanner;

public class BOJ2884 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hours = sc.nextInt();
        int minutes = sc.nextInt();
        int settedMinutes = hours * 60 + minutes - 45;
        if(settedMinutes < 0){
            settedMinutes += 24 * 60;
        }
        int newHours = (int)(settedMinutes / 60);
        int newMinutes = settedMinutes % 60;
        System.out.println(newHours + " " + newMinutes);

        sc.close();
    }
}

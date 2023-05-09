import java.util.Scanner;

public class BOJ2754 {
    enum Score{
        A(4), B(3), C(2), D(1), F(0);
        private final int point;

        Score(int point) { this.point = point; }
    
        public int getPoint() { return point; }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String scoreString = sc.nextLine();
        Score score = Score.valueOf(scoreString.charAt(0)+"");
        double point = score.getPoint();
        if( scoreString.length() == 2){
            String partialScore = scoreString.charAt(1) + "";
            if("+".equals(partialScore)){
                point += 0.3;
            }else if ("-".equals(partialScore)){
                point -= 0.3;
            }
        }
        System.out.println(point);
        
        sc.close();
    }

}

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BOJ2920 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] pitches = sc.nextLine().split(" ");
        List<Integer> arr = new ArrayList<>();
        int previous = 0;
        boolean isAsceding = true;
        boolean isMixed = false;
        for( int i=0; i< pitches.length ; i++){
            arr.add(Integer.parseInt(pitches[i]));
            int p = Integer.parseInt(pitches[i]);
            if( previous == 0){
                if( p == 8 ){
                    isAsceding = false;
                }else if( p == 1){
                    isAsceding = true;
                }else{
                    isMixed = true;
                    break;
                }                
            }else{
                int diff = isAsceding ? 1 : -1;
                if(previous + diff != p){
                    isMixed = true;
                    break;                    
                }
            }
            previous = p;
        }
        if(isMixed){
            System.out.println("mixed");
        }else if(isAsceding){
            System.out.println("ascending");
        }else{
            System.out.println("descending");
        }
        sc.close();
    }
}

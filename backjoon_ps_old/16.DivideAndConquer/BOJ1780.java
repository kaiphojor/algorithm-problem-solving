import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ1780 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            int N = Integer.parseInt(br.readLine());
            int[][] paper = new int[N][N];
            int standard = 0;
            boolean isSolid = true;
            for(int i=0; i<N ; i++){
                StringTokenizer st = new StringTokenizer(br.readLine()," ");
                for(int j=0; j<N; j++){
                    int number = Integer.parseInt(st.nextToken());
                    paper[i][j] = number;
                    
                    if(i ==0 && j == 0){
                        standard = number;
                    }else if(standard != number){
                        isSolid = false;
                    }
                }
            }

            if(isSolid){
                for(int i=-1 ; i<=1; i++){
                    if(i == standard){
                        bw.write(1+"\n");
                    }else{
                        bw.write(0+"\n");
                    }
                }
            }else{
                int[] paperCounts = countPaper(paper,0,0,N);
                for(int i=0; i<3; i++){
                    bw.write(paperCounts[i] + "\n");
                }
            }
            
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static int[] countPaper(int[][] paper, int x, int y, int n) {
        int oneThird = n / 3;
        int[] paperCounts = new int[3];
        if(oneThird > 0){
            for(int i=0; i<3; i++){
                for(int j=0; j<3; j++){
                    int nx = x + oneThird * i;
                    int ny = y + oneThird * j;
                    boolean isSolid = true;
                    int standard = paper[nx][ny];
                    for(int k=nx; k<nx+oneThird && isSolid; k++){
                        for(int l=ny; l<ny+oneThird; l++){
                            if(paper[k][l] != standard){
                                isSolid = false;
                                break;
                            }
                        }
                    }
                    if(isSolid){
                        paperCounts[standard+1] += 1;
                    }else{                        
                        int[] partialCounts = countPaper(paper, nx, ny, oneThird);
                        for(int a=0; a<3 ;a++){
                            paperCounts[a] += partialCounts[a];
                        }
                    }
                }
            }
        }
        return paperCounts;
    }
}

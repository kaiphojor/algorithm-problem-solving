import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ2630 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            int N = Integer.parseInt(br.readLine());
            int[][] O = new int[N][N];
            int[] origamiCount;
            int standard = -1;
            boolean isAllSameColor = true;
            for(int i=0; i<N ; i++){
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                for(int j=0; j<N; j++){
                    int tileColor = Integer.parseInt(st.nextToken());
                    if(i == 0 && j == 0){
                        standard = tileColor;
                    }else{
                        if(standard != tileColor){
                            isAllSameColor = false;
                        }
                    }
                    O[i][j] = tileColor;
                }
            }

            if(isAllSameColor){
                if(standard == 1){
                    origamiCount = new int[]{0,1};
                }else{
                    origamiCount = new int[]{1,0};
                }
            }else{                
                origamiCount = getCount(O, 0, 0, N);
            }
            
            bw.write(origamiCount[0] + "\n");
            bw.write(origamiCount[1] + "\n");
            
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static int[] getCount(int[][] m,int x,int y,int width){
        int[] dx = new int[]{0,1,0,1};
        int[] dy = new int[]{0,0,1,1};
        int half = width / 2;
        int[] paperCount = new int[2];
        if(half > 0){
            for(int i=0; i<4 ; i++){
                int nx = x + dx[i] * half;
                int ny = y + dy[i] * half;

                int standard = m[nx][ny];
                boolean isSame = true;
                for(int a=nx; a<nx+half ; a++){
                    for(int b=ny; b<ny+half; b++){
                        if(m[a][b] != standard){
                            isSame = false;
                            break;
                        }
                    }
                    if(!isSame){
                        break;
                    }
                }
                if(isSame){
                    paperCount[standard]+=1;
                }else{
                    int[] partialcount = getCount(m, nx, ny, half);
                    paperCount[0] += partialcount[0];
                    paperCount[1] += partialcount[1];
                }            
            }
        }
        return paperCount;
    }
    
}

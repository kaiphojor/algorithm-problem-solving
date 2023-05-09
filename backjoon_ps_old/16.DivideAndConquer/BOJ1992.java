import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ1992 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            int N = Integer.parseInt(br.readLine());
            int[][] arr = new int[N][N];
            
            for(int i=0; i<N; i++){
                String line = br.readLine().trim();
                for(int j=0; j<N; j++){
                    int number = Integer.parseInt(line.charAt(j)+"");
                    arr[i][j] = number;
                }
            }

            String result = drawQuadTree(arr,0,0,N);
            bw.write(result + "\n");
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static String drawQuadTree(int[][] arr, int a, int b, int n) {
        int standard = arr[a][b];
        boolean isSolid = true;
        for(int i=a; i<a+n && isSolid; i++){
            for(int j=b; j<b+n; j++){
                if(standard != arr[i][j]){
                    isSolid = false;
                }
            }
        }
        if(isSolid){
            return String.valueOf(standard);
        }else{
            int half = n / 2;
            int[] dx = new int[]{0,0,1,1};
            int[] dy = new int[]{0,1,0,1};
            StringBuilder sb = new StringBuilder();
            sb.append("(");

            for(int d=0; d<4; d++){
                int nx = a + dx[d] * half;
                int ny = b + dy[d] * half;
                standard = arr[nx][ny];
                boolean isPartSolid = true;

                for(int i=nx; i<nx+half && isPartSolid; i++){
                    for(int j=ny; j<ny+half; j++){
                        if(standard != arr[i][j]){
                            isPartSolid = false;
                        }                        
                    }
                }
                
                if(isPartSolid){
                    sb.append(standard);
                }else{
                    sb.append(drawQuadTree(arr, nx, ny, half));
                }
            }
            sb.append(")");            
            return sb.toString();
        }
    }
}

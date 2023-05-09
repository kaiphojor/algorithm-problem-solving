import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Tomato{
    int row;
    int col;
    public Tomato(int row, int col) {
        this.row = row;
        this.col = col;
    }
    public int getRow() {
        return row;
    }
    public int getCol() {
        return col;
    }    
}
public class BOJ7576 {
    public static void main(String[] args) {
        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int M = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int[][] board = new int[N][M];
            Queue<Tomato> queue = new LinkedList<>();
            for(int i=0; i<N; i++){
                st = new StringTokenizer(br.readLine()," ");
                for(int j=0; j<M ; j++){
                    board[i][j] = Integer.parseInt(st.nextToken());
                    if(board[i][j] == 1){
                        queue.add(new Tomato(i, j));
                    }
                }
            }
            int[] dx = new int[]{-1,1,0,0};
            int[] dy = new int[]{0,0,-1,1};
            while(!queue.isEmpty()){
                Tomato t = queue.poll();
                int x = t.getRow();
                int y = t.getCol();
                for(int d=0; d<4; d++){
                    int nx = x + dx[d];
                    int ny = y + dy[d];
                    if(0<=nx && nx<N && 0<= ny && ny<M){
                        if(board[nx][ny] == 0){
                            board[nx][ny] = board[x][y] + 1;
                            queue.add(new Tomato(nx, ny));
                        }
                    }
                }
            }

            int result = 0;
            for(int i=0; i<N  && result != -1; i++){
                for(int j=0; j<M && result != -1; j++){
                    if(board[i][j] == 0){
                        result = -1;
                    }else{
                        result = Math.max(result, board[i][j]);
                    }
                }
            }
            if(result > 0){
                result--;
            }
            bw.write(result +"\n");            
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

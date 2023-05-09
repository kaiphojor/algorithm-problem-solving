public class LEETCODE200 {
    class Solution {
        public int numIslands(char[][] grid) {
            int row = grid.length;
            int col = grid[0].length;
            boolean[][] visited = new boolean[row][col];
            int islandCount = 0;
            for(int i=0; i<row; i++){
                for(int j=0; j<col; j++){
                    if(grid[i][j] == '1' && !visited[i][j]){
                        dfs(grid,visited,i,j);
                        islandCount++;
                    }
                }
            }
            return islandCount;
        }
        void dfs(char[][] grid, boolean[][] visited, int x, int y){
            visited[x][y] = true;
            int[] dx = new int[]{-1,1,0,0};
            int[] dy = new int[]{0,0,-1,1};
            for(int i=0; i<4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx>=0 && nx<grid.length && ny>=0 && ny<grid[0].length){
                    if(grid[nx][ny] == '1' && !visited[nx][ny]){
                        dfs(grid,visited,nx,ny);
                    }
                }
            }
        }
    }
}

public class LEETCODE733 {
    class Solution {
        public int[][] floodFill(int[][] image, int sr, int sc, int color) {
            int srcColor = image[sr][sc];
            if(srcColor != color){
                dfs(image,sr,sc,srcColor,color);    
            }
            
            return image;
        }
        void dfs(int[][] image, int sr, int sc, int srcColor,int destColor){
            image[sr][sc] = destColor;
            int[] dx = new int[]{-1,1,0,0};
            int[] dy = new int[]{0,0,-1,1};
            for(int i=0; i<4; i++){
                int nx = sr + dx[i];
                int ny = sc + dy[i];
                if(nx >=0 && nx< image.length && ny >=0 && ny <image[0].length){
                    if(image[nx][ny] == srcColor){
                        dfs(image,nx,ny,srcColor,destColor);
                    }
                }
            }
            
        }
    }
}

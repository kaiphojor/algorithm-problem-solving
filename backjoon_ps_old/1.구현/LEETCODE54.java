class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[] dx = new int[]{0,1,0,-1};
        int[] dy = new int[]{1,0,-1,0};
        List<Integer> spiralList = new ArrayList<>();
        int width = n;
        int height = m;
        int x = 0;
        int y = -1;
        int d = -1;
        while(true){
            d++;
            d = d >= 4? d-4: d;
            for(int i=0;i<width;i++){
                y += dy[d];
                spiralList.add(matrix[x][y]);
            }
            width--;
            if(width <= n-m){
                break;
            }
            d++;
            d = d >= 4? d-4: d;
            height--;
            for(int i=0;i<height;i++){
                x += dx[d];
                spiralList.add(matrix[x][y]);
            }
            if(height == m-n){
                break;
            }
        }
        return spiralList;
    }
}
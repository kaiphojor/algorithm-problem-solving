/*
1 1
2 1 1 2 
3 3
4 5 
*/
class Solution {
    public int climbStairs(int n) {
        if(n <= 2){
            return n;
        }
        int[] stairCases = new int[n+1];
        stairCases[1] = 1;
        stairCases[2] = 2;
        for(int i=3; i<=n; i++){
            stairCases[i] = stairCases[i-1] + stairCases[i-2]; 
        }
        return stairCases[n];
    }
}
public class LEETCODE70 {
    
}

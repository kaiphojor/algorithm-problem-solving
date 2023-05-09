class Solution {
    public boolean isHappy(int n) {
        return isHappyWithoutCycle(new ArrayList<>(),n);
    }
    boolean isHappyWithoutCycle(List<Integer> list,int n){
        if(n == 1 ){
            return true;
        }
        int sumOfSquared = 0;
        for(char c : String.valueOf(n).toCharArray()){
            sumOfSquared += Math.pow(c-'0',2);
        }
        if(list.contains(sumOfSquared)){
            return false;
        }
        list.add(sumOfSquared);
        return isHappyWithoutCycle(list, sumOfSquared);
    }
}
public class LEETCODE202 {
    
}

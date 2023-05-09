class Solution {
    public boolean backspaceCompare(String s, String t) {
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        ArrayList<Character> sList = new ArrayList<Character>();
        ArrayList<Character> tList = new ArrayList<Character>();
        for(char c : sArr){
            if(c == '#'){
                if(sList.size() > 0){
                    sList.remove(sList.size()-1);
                }
            }else{
                sList.add(c);
            }
        }
        for(char c : tArr){
            if(c == '#'){
                if(tList.size() > 0){
                    tList.remove(tList.size()-1);
                }
            }else{
                tList.add(c);
            }
        }
        
        if(sList.size() != tList.size()){
            return false;
        }else{
            for(int i=0; i<sList.size(); i++){
                if(sList.get(i) != tList.get(i)){
                    return false;
                }
            }
            return true;
        }
    }
}
public class LEETCODE844 {
    
}

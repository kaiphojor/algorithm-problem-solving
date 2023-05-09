class Solution {
    public String getHint(String secret, String guess) {
        char[] sArr = secret.toCharArray();
        char[] gArr = guess.toCharArray();
        int aCount = 0;
        int bCount = 0;
        Map<Character,Integer> sMap = new HashMap<Character,Integer>();
        Map<Character,Integer> gMap = new HashMap<Character,Integer>();
        for(int i=0; i<sArr.length ; i++){
            if(sArr[i] == gArr[i]){
                aCount++;
            }else{
                if(sMap.get(sArr[i]) == null){
                    sMap.put(sArr[i],1);
                }else{
                    sMap.put(sArr[i],sMap.get(sArr[i])+1);
                }
                if(gMap.get(gArr[i]) == null){
                    gMap.put(gArr[i],1);
                }else{
                    gMap.put(gArr[i],gMap.get(gArr[i])+1);
                }
            }
        }
        for(char key : sMap.keySet()){
            if(gMap.get(key) != null){
                int sCount = sMap.get(key);
                int gCount = gMap.get(key);
                if(sCount >= gCount){
                    bCount += gCount;
                }else{
                    bCount += sCount;
                }
            }
        }
        return aCount + "A" + bCount + "B";
    }
}
public class LEETCODE299 {
    
}

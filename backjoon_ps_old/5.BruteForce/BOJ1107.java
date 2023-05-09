import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

/*
 * 가장 가까운 채널 고르기
 * 가장 가까운 채널 중 채널이 안막힌 것 찾기
 */
public class BOJ1107 {
    public static void main(String[] args) {

        try (
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ) {
            int startChannel = 100;
            int destinationChannel = Integer.parseInt(br.readLine().trim());
            int blockButtonCount = Integer.parseInt(br.readLine().trim());
            Set<String> blockedSet = new HashSet<>();
            if(blockButtonCount != 0){
                StringTokenizer st = new StringTokenizer(br.readLine()," ");
                for(int i=0; i<blockButtonCount ;i++){
                    blockedSet.add(st.nextToken());
                }
            }
            int closestChannel = 500000;
            int gap = 0;
            while(true){
                boolean isUpperChannelValid = true;
                boolean isLowerChannelValid = true;
                boolean isUpperChannelClosest = false;
                String[] numberStrings = String.valueOf(destinationChannel + gap).split("");
                Set<String> numberSets = new HashSet<String>();
                Collections.addAll(numberSets, numberStrings);
                String[] numberArr = numberSets.toArray(new String[0]);
                for(String str : numberArr){
                    if(blockedSet.contains(str)){
                        isUpperChannelValid = false;
                        isUpperChannelClosest = false;
                        break;
                    }
                }
                if(isUpperChannelValid){
                    isUpperChannelClosest = true;
                }
                if(destinationChannel -gap >= 0){
                    numberStrings = String.valueOf(destinationChannel - gap).split("");
                    numberSets = new HashSet<String>();
                    Collections.addAll(numberSets, numberStrings);
                    for(String str : numberSets.toArray(new String[0])){
                        if(blockedSet.contains(str)){
                            isLowerChannelValid = false;
                            isUpperChannelClosest = true;
                            break;
                        }
                    }
                    if(isLowerChannelValid){
                        isUpperChannelClosest = false;
                    }
                }else{
                    isLowerChannelValid = false;
                }

                if(isUpperChannelValid || isLowerChannelValid){
                    closestChannel = isUpperChannelClosest ? destinationChannel + gap : destinationChannel - gap;

                    break;
                }
                if(gap > 499900){
                    gap += 500000;
                    break;
                }
                gap++;
            }


            int moveOnlyCount = (int)Math.abs(startChannel-destinationChannel);
            int channelSelectCount = gap + String.valueOf(closestChannel).length();
            
            int result = Math.min(moveOnlyCount,channelSelectCount);
            bw.write(result + "\n");
            bw.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}

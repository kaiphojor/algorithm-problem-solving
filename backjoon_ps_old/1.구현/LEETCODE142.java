import java.util.ArrayList;
import java.util.List;

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
class Solution {
    public ListNode detectCycle(ListNode head) {
        List<ListNode> list = new ArrayList<ListNode>();
        while(head != null){
            if(list.contains(head)){
                return head;
            }else{
                list.add(head);
            }            
            head = head.next;
        }
        return null;
    }
}
public class LEETCODE142 {
    
}

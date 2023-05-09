/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode middleNode = head;
        ListNode lastNode = head.next;
        
        while(lastNode != null){
            middleNode = middleNode.next;
            lastNode = lastNode.next;
            if(lastNode != null){
                lastNode = lastNode.next;
            }
        }
        
        return middleNode;        
    }
}
public class LEETCODE876 {
    
}

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
    public ListNode reverseList(ListNode head) {
        ListNode previous, current;
        current = null;
        while(head != null){
            previous = current;
            current = head;
            head = head.next;
            current.next = previous;            
        }
        return current;
    }
}
public class LEETCODE206 {
    
}

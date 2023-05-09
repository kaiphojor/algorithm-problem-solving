class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode(-101);
        ListNode pointer = head;
        while(list1 != null && list2 != null){
            if(list1.val < list2.val){                
                pointer.next = list1;
                list1 = list1.next;
            }else{
                pointer.next = list2;
                list2 = list2.next;
            }
            pointer = pointer.next;
        }
        if(list1 != null){
            pointer.next = list1;
        }
        if(list2 != null){
            pointer.next = list2;
        }
        return head.next;
    }
}
public class LEETCODE21 {
    Solution s = new Solution();
    ListNode l1 = new ListNode();
    ListNode l2 = new ListNode();
    ListNode l3 = s.mergeTwoLists(l1, l2);
}

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        odd = head
        even_head = even = head.next
        isOdd = True
        cur = even.next
        while cur != None:
            if isOdd:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next
            isOdd = not isOdd
        odd.next = even_head
        even.next = None
        return head
        
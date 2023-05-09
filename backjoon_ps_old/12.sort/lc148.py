# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        cur = head        
        while cur != None:            
            li.append(cur.val)
            cur = cur.next
        li.sort()
        cur = head
        idx = 0
        while cur != None:            
            cur.val = li[idx]
            cur = cur.next
            idx += 1
        return head
            
        
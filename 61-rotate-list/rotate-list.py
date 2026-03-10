# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        curr , n = head , 1
        while curr.next:
            n+=1 
            curr = curr.next
        
        curr.next = head
        k%=n

        for i in range(n-k):
            curr=curr.next
        
        head = curr.next
        curr.next = None
    
        return head
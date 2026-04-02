# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point
        # reverse and keep the mid +1 part
        # then join it
        slow, fast=head, head
        while fast and fast.next:
            slow = slow.next
            fast = (fast.next).next
        
        # reverse it
        curr = slow.next
        prev = slow.next = None
    
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # prev will hold the head now of the second part
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


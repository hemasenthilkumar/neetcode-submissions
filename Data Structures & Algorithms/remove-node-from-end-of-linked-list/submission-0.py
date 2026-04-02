# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length
        # calculate node from start => len - n + 1
        # traverse till the prev node, prev to none, move 1+1 when node stadsn on the nth node, 
        # connect the prev.next to node.next
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        remove_at = length - n
        prev, node = head, head.next
        start = 0
        dummy = ListNode()
        dummy.next = head
        prev, node = dummy, head
        for _ in range(remove_at):
            prev = prev.next
            node = node.next

        prev.next = node.next
        node.next = None
        return dummy.next
        
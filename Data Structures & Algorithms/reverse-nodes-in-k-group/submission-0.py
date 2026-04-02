# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_k_nodes(head, k):
            prev, curr = None, head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, curr
        
        dummy = ListNode(0, head)
        ptr = dummy

        while ptr:
            tracker = ptr
            for _ in range(k):
                if not tracker:
                    break
                tracker = tracker.next
            if not tracker:
                break
            prev, curr = reverse_k_nodes(ptr.next, k)

            last_node_of_prev_group = ptr.next
            ptr.next = prev
            last_node_of_prev_group.next = curr
            ptr = last_node_of_prev_group

        return dummy.next

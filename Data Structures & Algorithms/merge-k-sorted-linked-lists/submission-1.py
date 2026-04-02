# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # method for merging 2 lists and return the final list
        # run this method initially for top 2 lists, 
        # then loop from 2:k and send the prev with each next.
        if not lists or len(lists) ==0:
            return None
        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            prev = dummy
            while l1 and l2:
                a = l1.val
                b = l2.val
                if a <= b:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next= l2
                    l2 = l2.next
                prev = prev.next
            prev.next = l1 if l1 else l2
            return dummy.next

        prev = lists[0]
        for lis in lists[1:]:
            prev = mergeTwoLists(prev, lis)
        return prev
        
        

        
    
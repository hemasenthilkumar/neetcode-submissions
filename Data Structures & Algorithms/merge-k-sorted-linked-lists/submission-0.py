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
                a = l1.val if l1 else 0
                b = l2.val if l2 else 0
                if a <= b:
                    curr = ListNode(a)
                    if l1:
                        l1 = l1.next
                else:
                    curr = ListNode(b)
                    if l2:
                        l2 = l2.next
                prev.next = curr
                prev = curr
                if not l1:
                    while l2:
                        curr =  ListNode(l2.val)
                        prev.next = curr
                        prev = curr
                        l2 = l2.next
                    break
                if not l2:
                    while l1:
                        curr =  ListNode(l1.val)
                        prev.next = curr
                        prev = curr
                        l1 = l1.next
                    break
            return dummy.next

        prev = mergeTwoLists(lists[0], lists[1])
        for lis in lists[2:]:
            curr = mergeTwoLists(prev, lis)
            prev = curr
        return prev
        
        

        
    